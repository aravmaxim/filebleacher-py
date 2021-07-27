BMP_HEADER_SIZE = 14
BMP_MAGIC_NUMBERS = {
    'BM': 'Windows 3.1x, 95, NT, ... etc',
    'BA': 'OS/2 struct bitmap array',
    'CI': 'OS/2 struct color icon',
    'CP': 'OS/2 const color pointer',
    'IC': 'OS/2 struct icon',
    'PT': 'OS/2 pointer'
}

BITMAPCOREHEADER_SIZE = 12
BITMAPCOREHEADER2_SIZE = 64
OS22XBITMAPHEADER_SIZE = 16
BITMAPINFOHEADER_SIZE = 40
BITMAPV2INFOHEADER_SIZE = 52
BITMAPV3INFOHEADER_SIZE = 56
BITMAPV4HEADER_SIZE = 108
BITMAPV5HEADER_SIZE = 124

DIB_HEADER_TYPES = {
  BITMAPCOREHEADER_SIZE : 'BITMAPCOREHEADER',
  BITMAPCOREHEADER2_SIZE : 'BITMAPCOREHEADER2',
  OS22XBITMAPHEADER_SIZE : 'OS22XBITMAPHEADER',
  BITMAPINFOHEADER_SIZE : 'BITMAPINFOHEADER',
  BITMAPV2INFOHEADER_SIZE : 'BITMAPV2INFOHEADER',
  BITMAPV3INFOHEADER_SIZE : 'BITMAPV3INFOHEADER',
  BITMAPV4HEADER_SIZE : 'BITMAPV4HEADER',
  BITMAPV5HEADER_SIZE : 'BITMAPV5HEADER'
}

def __read_bmp_header(data : bytes) -> dict:
  header_data : bytes = data[:BMP_HEADER_SIZE]
  bmpHeader = { 
    'magic_number' : (header_data[:2]).decode("ascii") ,
    'bmp_size' : int.from_bytes(header_data[2:6], byteorder='little', signed=False),
    'reserved1' : int.from_bytes(header_data[6:8], byteorder='little', signed=False),
    'reserved2' : int.from_bytes(header_data[8:10], byteorder='little', signed=False),
    'offset_to_data' : int.from_bytes(header_data[10:14], byteorder='little', signed=False)
  }
  return bmpHeader

def __check_bmp_header(data : bytes, bmpHeader : dict) -> bool:
  if (bmpHeader['magic_number'] not in BMP_MAGIC_NUMBERS):
    print('Bad Magic number:%s' % bmpHeader['magic_number'])
    return False
  
  if (bmpHeader['bmp_size'] != len(data)):
    print('Bad BMP length expected %d got %d' % (bmpHeader['bmp_size'], len(data)))
    return False

  if (bmpHeader['reserved1'] != 0 or bmpHeader['reserved2'] != 0):
    print('Bad reserved')
    return False

  if (bmpHeader['offset_to_data'] > len(data)):
    print('Bad offset')
    return False

  return True

def __read_dib_header(data : bytes) -> dict:
  if (len(data) < BMP_HEADER_SIZE + 4):
    return None
  
  dib_size = int.from_bytes(data[BMP_HEADER_SIZE:BMP_HEADER_SIZE + 4], byteorder='little', signed=False)

  if dib_size not in DIB_HEADER_TYPES:
    return None
  
  if (len(data) < BMP_HEADER_SIZE + dib_size):
    return None

  dib_type = DIB_HEADER_TYPES[dib_size]

  if dib_type == 'BITMAPINFOHEADER':
    return __read_BITMAPINFOHEADER(data[BMP_HEADER_SIZE: BMP_HEADER_SIZE + dib_size])
  
  return None

def __read_BITMAPINFOHEADER(data : bytes) -> dict:
  header = {
    'type' : 'BITMAPINFOHEADER',
    'width' : int.from_bytes(data[4:8], byteorder='little', signed=False),
    'height ' : int.from_bytes(data[8:12], byteorder='little', signed=False),
    'color_planes' : int.from_bytes(data[12:14], byteorder='little', signed=False),
    'bits_per_pixel' : int.from_bytes(data[14:16], byteorder='little', signed=False),
    'compression_method' : int.from_bytes(data[16:20], byteorder='little', signed=False),
    'image_size' : int.from_bytes(data[20:24], byteorder='little', signed=False),
    'horizontal_resolution' : int.from_bytes(data[24:28], byteorder='little', signed=False),
    'vertical_resolution' : int.from_bytes(data[28:32], byteorder='little', signed=False),
    'number_of_colors' : int.from_bytes(data[32:36], byteorder='little', signed=False),
    'number_of_important_colors' : int.from_bytes(data[36:40], byteorder='little', signed=False)
  }

  return header

def __check_dib_header(data : bytes, dib_header : dict) -> bool:
  if dib_header['type'] == 'BITMAPINFOHEADER':
    return __check_BITMAPINFOHEADER(data, dib_header)
  
  return False

def __check_BITMAPINFOHEADER(data : bytes, dib_header : dict) -> bool:
  # TODO : implament
  
  return True

def __check_data(data : bytes, bmp_header : dict, dib_header : dict) -> bool:
  # TODO : implament
  
  return True

def check_bmp(data : bytes, opts: dict) -> bool:
  """Checks given bitmap file data for format coplince

  Parameters:
  data (bytes): bitmap file data
  opts (dict): dictionary contains configuration

  Returns:
  bool: If true file format is ok, else false
  """
  # Check minmum size for BMP header
  if (len(data) < BMP_HEADER_SIZE):
    return False

  # Read bmp header
  bmpHeader = __read_bmp_header(data)

  # Check bmp header
  if(not __check_bmp_header(data, bmpHeader)):
    return False

  # Reads dib header
  dib_header = __read_dib_header(data)

  # Check if readed dib header
  if dib_header == None:
    return False

  # Checks dib header
  if not __check_dib_header(data, dib_header):
    return False

  # Check data
  if not __check_data(data, bmpHeader, dib_header):
    return False

  return True

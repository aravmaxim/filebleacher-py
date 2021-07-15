import struct

BMP_HEADER_SIZE = 14
BMP_MAGIC_NUMBERS = {
    'BM': 'Windows 3.1x, 95, NT, ... etc',
    'BA': 'OS/2 struct bitmap array',
    'CI': 'OS/2 struct color icon',
    'CP': 'OS/2 const color pointer',
    'IC': 'OS/2 struct icon',
    'PT': 'OS/2 pointer'
}

def __read_bmp_header(data) -> dict:
  parsed_data = struct.unpack('ccIhhh', data[:BMP_HEADER_SIZE])
  bmpHeader = { 
    'magic_number' : parsed_data[0] + parsed_data[1],
    'bmp_size' : parsed_data[2],
    'reserved1' : parsed_data[3],
    'reserved2' : parsed_data[4],
    'offset_to_data' : parsed_data[5]
  }
  return bmpHeader

def __check_bmp_header(data : bytes, bmpHeader : dict) -> bool:
  if (bmpHeader['magic_number'] not in BMP_MAGIC_NUMBERS):
    return False
  
  if (bmpHeader['bmp_size'] != len(data)):
    return False

  return True

def check_bmp(data : bytes, opts: dict) -> bool:
  # Check minmum size for BMP header
  if (len(data) < BMP_HEADER_SIZE):
    return False

  # Read bmp header
  bmpHeader = __read_bmp_header(data)
  
  # TODO : Raed BMP header
  # TODO : Check BMP header
  # TODO : Check DIB header size
  # TODO : Read DIB header
  # TODO : Check DIB header
  # TODO : Check data
  return True

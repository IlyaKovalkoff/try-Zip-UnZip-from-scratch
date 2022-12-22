import sys


source_file_name = sys.argv[1]
target_file_name = sys.argv[2]

def sizeof(number):
  bytes = 0
  while number!=0:
    number >>= 8
    bytes += 1
  return bytes

def tlv(number):
    barr = bytearray()
    barr.extend((sizeof(number)).to_bytes(1, 'big'))
    barr.extend(number.to_bytes(sizeof(number), 'big'))
    return barr 

def compression(src_file,fin_file):
    symbol = src_file.read(1) #
    dictionary_size = 256          
    dictionary_self_made_by_unicode = {chr(dictionary_simbol) : dictionary_simbol for dictionary_simbol in range(dictionary_size)}

    step_of_compression = ''
    
    while symbol:
        
        simbol_and_next_simbol = step_of_compression + symbol 

        

        if simbol_and_next_simbol in dictionary_self_made_by_unicode:
            step_of_compression = simbol_and_next_simbol

        else:
                
            x = tlv(dictionary_self_made_by_unicode[step_of_compression])
            print(x)
            fin_file.write(x)
            dictionary_self_made_by_unicode[simbol_and_next_simbol] = dictionary_size
            dictionary_size += 1
            step_of_compression = symbol 

        

        symbol = src_file.read(1)

    if step_of_compression != False:
        x = tlv(dictionary_self_made_by_unicode[step_of_compression])
        fin_file.write(x)
    #print (dictionary_self_made_by_unicode)

with open(source_file_name,'rt') as source_file: #
    with open(target_file_name + '._zipped_by_Ilysha', 'wb') as finnal_file:
        compression(source_file,finnal_file)
    








import sys


def sumbol(source_file):
    length = int.from_bytes(source_file.read(1),'big')
    value = int.from_bytes(source_file.read(length),'big')
    return value

def decompression(src_file,fin_file):
    symbol = sumbol(src_file)
    dictionary_size = 256
    dictionary_self_made_by_unicode = {chr(dictionary_simbol) : dictionary_simbol for dictionary_simbol in range(dictionary_size)}
    dictionary_self_made_by_unicode_1 = {dictionary_simbol : chr(dictionary_simbol) for dictionary_simbol in range(dictionary_size)}

 
    step_of_decompression = ''
    previous_symbols = dictionary_self_made_by_unicode_1[symbol]
    fin_file.write(dictionary_self_made_by_unicode_1[symbol])
    

    while symbol != 0:
        
       

        if previous_symbols in dictionary_self_made_by_unicode:
            step_of_decompression = previous_symbols
         
            
        else:
            dictionary_self_made_by_unicode[previous_symbols] = dictionary_size
            dictionary_self_made_by_unicode_1[dictionary_size] = previous_symbols
            error = dictionary_self_made_by_unicode_1[dictionary_size] 
            step_of_decompression = dictionary_self_made_by_unicode_1[symbol]
            dictionary_size += 1
            
                
            
            
        symbol = sumbol(src_file) 
   
        if symbol in dictionary_self_made_by_unicode_1:   
            previous_symbols = step_of_decompression + ((dictionary_self_made_by_unicode_1[symbol])[0])

            fin_file.write(dictionary_self_made_by_unicode_1[symbol])
        
        else:
            dictionary_self_made_by_unicode_1[symbol] = error + error[0] 
 
            dictionary_self_made_by_unicode[dictionary_self_made_by_unicode_1[symbol]] = dictionary_size
            
            
            dictionary_size += 1
            step_of_decompression = dictionary_self_made_by_unicode_1[symbol]
            previous_symbols = dictionary_self_made_by_unicode_1[symbol]
            fin_file.write(dictionary_self_made_by_unicode_1[symbol])
        
  
     
             

        

    
    
with open('c:\\Users\\ASUS\\Desktop\\rararhivator_my\\files_to_zip\\edeegr._zipped_by_Ilysha ','rb') as source_file:
    
    with open ('c:\\Users\\ASUS\\Desktop\\rararhivator_my\\files_to_zip\\done.txt', 'wt') as target_file:
        decompression(source_file,target_file)
    


    #value = source_file.read(int(length))
    #with open(target_file_name + '._zipped_by_Ilysha', 'wb') as finnal_file:
        #compression(source_file,finnal_file)
  
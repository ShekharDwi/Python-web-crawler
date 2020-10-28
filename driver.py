import os

def exe(comm):
	if (comm == 1):
		os.system('python spider.py')
	elif (comm == 2):
		os.system('python rankalgo.py')
	elif (comm == 3):
		os.system('python rankreset.py')
	elif (comm == 4):
		os.system('python datadump.py')
	elif (comm == 5):
		os.system('python jsonexport.py')
	elif (comm == 6):
		os.system('force.html')
	elif (comm == 7):
		print("Are you sure you want to delete file \"spider.sqlite\" ? (y/n)")
		sure = input()
		if sure=="y":
			try:
				os.remove("spider.sqlite")
				print("\n **File Sucessfully Deleted\n")
			except:
				print("** ERROR: File Not Found")
		elif sure=="n":
			return
		
		
	elif (comm == 8):
		exit()
	

print("\n Welcome to Search Ranker")

print("""           ;               ,           
         ,;                 '.         
        ;:                   :;        
       ::                     ::       
       ::                     ::       
       ':                     :        
        :.                    :        
     ;' ::                   ::  '     
    .'  ';                   ;'  '.    
   ::    :;                 ;:    ::   
   ;      :;.             ,;:     ::   
   :;      :;:           ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'    
        '''""....;:::::;,;.;''""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..         :;  
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':.
::     ;:"  :::::::""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;  
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:        
        ':;                 ;:"        
          ';              ,;'          
            "'           '"            
              ' """)


while True:
	print("\n Please choose your option")
	print("1. Start/Resume Crawler")
	print("2. Start PageRanking Program")
	print("3. Reset Page Ranks")
	print("4. Dump raw database entries")
	print("5. Export database to JSON")
	print("6. Visualize Database")
	print("7. Delete Database (Use with Caution)")
	print("8. Exit\n")
	comm = int(input())
	exe(comm)
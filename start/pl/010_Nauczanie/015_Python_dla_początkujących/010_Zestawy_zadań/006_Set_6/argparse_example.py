import argparse

import os

SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("password" , 
                        help = 
                        "Secret password used to encrypt / decript notes.")
    parser.add_argument("--key" , "-k" , 
                        help = "Keyword for note" , action = 'append')
    parser.add_argument("--print" , "-p" ,
                        help = "Print all saved notes." , action = "store_true")
    parser.add_argument("--printany" , "-a" ,
                        help = "Print all note that contain any of the keywords." , 
                        action = "store_true")
    parser.add_argument("--printall" , "-o" ,
                        help = "Print only the notes that contain all the keywords" , 
                        action = "store_true")
    parser.add_argument("--new" , "-n" ,
                        help = "Add new note." , 
                        action = "store_true")
    parser.add_argument("--delete" , "-d" ,
                        help = "Deletes note with given number." ,
                        type = int)
    args = parser.parse_args()    

    print("password : " , args.password)
    print("keywords : " , args.key)

    if args.print:
        print("... Printing all notes ...")
    if args.printany:
        print("... Printing all notes that contain ANY of the keywords ...")
    if args.printall:
        print("... Printing all notes that contain ALL of the keywords ...")
    if args.new:
        print("... Please enter note and keywords ...")
        path_to_note = os.path.join(SCRIPTDIR , "note_file")
        print("... Note saved to : " , path_to_note , "...")
    if args.delete is not None:
        print("... Deleting note number " , args.delete , "...")
        print(type(args.delete))



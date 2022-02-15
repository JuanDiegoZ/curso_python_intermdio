# function to iterate the diccionary and print it
def diccionary_value(dict):
        for key,value in dict.items():
            print(key," - ",value)
# function to iterate the list and print it
def array_value(list):
        for i in list:
            print(i)

# Main, contains the list and dictionary in the exercise. 
# Call out all funcions
def run():
    my_list =[]
    my_dic ={"firstname":"Pepe","lastname":"Garcia" }

    super_list =[
        {"firstname":"Ana","lastname":"Nuñes" },
        {"firstname":"Pepe","lastname":"Garcia" },
        {"firstname":"Pepita","lastname":"Rodrigez" }
    ]

    super_dict ={
        "fruit":     ["apple","banana","melon","pinneappple","sweetberry"],
        "vegetables":["onion","brokoly","carrot","potato","cucumber"]
    }
    diccionary_value(super_dict)
    array_value(super_list)

if __name__ == "__main__":
    run()

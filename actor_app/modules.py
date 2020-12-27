# functions to be used by the routes

# retrieve all the names from the dataset and put them into a list
def get_names(source):
    names = []
    for row in source:
        # lowercase all the names for better searching
        name = row["Name"].lower()
        names.append(name)
    return sorted(names)

# find the row that matches the id in the URL, retrieve name and photo
def get_actor(source, id, type):
    import qrcode
    
    print(type)
    
    if type == "Component":
        
        for row in source:
            name = row["Name"]
            #Generate QR Code, save it, and return the location of the qr
            qr = "qr_Component" +  id + ".jpg"
            
            #QR code is generated as the page of the webpage
            path =  '/module/' + id
            img = qrcode.make(path)
            
            img.save("qr_Inventory" +  id + ".jpg")
            
            # change number to string
            id = str(id)
            # return these if id is valid
            return id, name, qr
    elif type == "Inventory":
        
        for row in source:
            if id == str( row["BOM ID"] ):
                name = row["Name"]
    
                #Generate QR Code, save it, and return the location of the qr
                qr = "qr_" +  id + ".jpg"
                
                #QR code is generated as the page of the webpage
                path =  '/module/' + id
                img = qrcode.make(path)
                
                img.save("qr_Component" +  id + ".jpg")
                
                # change number to string
                id = str(id)
                # return these if id is valid
                return id, name, qr
    # return these if id is not valid - not a great solution, but simple
    return "Unknown", "Unknown", ""

# find the row that matches the name in the form and retrieve matching id
def get_id(source, name, type):
    if(type == "Component"):
         for row in source:
            # lower() makes the string all lowercase
            if name.lower() == row["Name"].lower():
                id = row["Component ID"]
                # change number to string
                id = str(id)
                # return id if name is valid
                return id
    else:
        for row in source:
            # lower() makes the string all lowercase
            if name.lower() == row["Name"].lower():
                id = row["BOM ID"]
                # change number to string
                id = str(id)
                # return id if name is valid
                return id
    # return these if id is not valid - not a great solution, but simple
    return "Unknown"

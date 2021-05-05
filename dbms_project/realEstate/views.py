from django.shortcuts import render, HttpResponse
from django.db import connection
from collections import namedtuple
from datetime import date

dataunique = {}

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# Create your views here.
def index(request):
    return HttpResponse("testing purpose")

def Customer(request):
    # lis = []
    # cursor = connection.cursor()
    # cursor.execute("select distinct locality from address")
    # for i in cursor:
    #     lis.append(i)
    # print(lis)

    # form data
    if request.method=="POST":
        salerent = request.POST.get('salerent', '')
        htype = request.POST.get('htype', '')
        areamin = request.POST.get('areamin', '')
        areamax = request.POST.get('areamax', '')
        bhk = request.POST.get('bhk', '')
        pricemin = request.POST.get('pricemin', '')
        pricemax = request.POST.get('pricemax', '')
        print(salerent, htype, areamin, areamax, bhk, pricemin, pricemax) 

        lis = []
        cursor = connection.cursor()
        cursor.execute("select selling_price, plot_area, bhk, parking_available, owner, status, Agent.name, Contact, Number_of_Properties_Sold, Number_of_properties_rented, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Status = 'available' AND Available_For = " +"'" + salerent + "'" + " AND type = " +"'" + htype + "'" + " AND Plot_Area >= " + areamin + " AND Plot_Area <= " + areamax + " AND BHK = " + bhk + " AND selling_Price >=  " + pricemin + " AND selling_Price <= " + pricemax)
        # cursor.execute("select selling_price, plot_area, bhk, parking_available, owner, status, Agent.name from estate natural join agent")
        for i in cursor:
            lis.append(i)
        print(lis)    
        
        data = {
            'arr': lis
        }

        return render(request, 'realEstate/Buyer.html', data)
    else:    
        return render(request, 'realEstate/Buyer.html')

def Administrator(request):
    if request.method == "POST":
        if 'op1' in request.POST:
            propertyBased = request.POST.get('propertyBased', '')
            print("*****")
            print(propertyBased)
            print("*****")
            lis = []
            cursor = connection.cursor()
            if propertyBased == 'AFR':
                cursor.execute("select serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, type, locality, status, Available_For, Date_of_Sale_OR_Rent from estate natural join address where Available_for = 'Rent' and Status = 'Available'")
            elif propertyBased == 'AFS':
                cursor.execute("select serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, type, locality, status, Available_For, Date_of_Sale_OR_Rent from estate natural join address where Available_for = 'Sale' and Status = 'Available'")    
            elif propertyBased == 'Rented':
                cursor.execute("select serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, type, locality, status, Available_For, Date_of_Sale_OR_Rent from estate natural join address where Available_for = 'Rent' and Status = 'Rented'")
            elif propertyBased == 'Sold':
                cursor.execute("select serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, type, locality, status, Available_For, Date_of_Sale_OR_Rent from estate natural join address where Available_for = 'Sale' and Status = 'Sold'")
            for i in cursor:
                lis.append(i)
            
            # agent details
            serial = []
            results = namedtuplefetchall(cursor)
            # print(results)
            for i in range(len(results)):
                serial.append(results[i].serial_No)
            print("******agent")
            print(serial)
            print("agent ************")

            agentDetails = []
            for j in serial:
                j = str(j)
                cursor.execute("Select Name, Contact, Number_of_Properties_Sold, Number_of_properties_rented from agent natural join estate where serial_no = " + j)
                for i in cursor:

                    agentDetails.append(i)
            print("!!!!!!!!!!!!!!!")
            print(agentDetails)
            print("!!!!!!!!!!!!!!!")
            # agent details (USED LATER AFTER IN POPUPS)
  
            data = {
                'filter': 'propBased',
                'arr': lis,
                'agentdetails': agentDetails 
            }  
            # print(data)      
            return render(request, 'realEstate/admin.html', data) 

        elif 'op2' in request.POST:
            agentBased = request.POST.get('agentBased', '')
            print("*****")
            print(agentBased)
            print("*****")       
        
            lis = []

            # fetching agentID
            ID = []
            cursor = connection.cursor()
            cursor.execute("select Agent_ID from agent where Name = '" + agentBased + "'")
            results = namedtuplefetchall(cursor)
            ID.append(results[0].Agent_ID)
            print(ID)

            agentID = ID[0]
            agentID = str(agentID)
            cursor = connection.cursor()
            cursor.execute("select selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality, Date_of_Sale_OR_Rent from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + agentID)
            for i in cursor:
                lis.append(i)
            print(lis)
            
            data = {
                'filter': 'agentBased',
                'arr': lis
            }    

            return render(request, 'realEstate/admin.html', data)     
    else:        
        return render(request, 'realEstate/admin.html')            

def Agent(request):
    global dataunique
    if request.method == "POST":
        if 'addProperty' in request.POST:
            agentID = request.POST.get('agent', '')
            userID = request.POST.get('user', '')
            availFor = request.POST.get('avail', '')
            # status = request.POST.get('status', '')
            price = request.POST.get('price', '')
            bhk = request.POST.get('bhk', '')
            gender = request.POST.get('gender', '')
            area = request.POST.get('area', '')
            parking = request.POST.get('parking', '')
            owner = request.POST.get('owner', '')
            locality = request.POST.get('locality', '')
            pin = request.POST.get('pin', '')
                
            print(agentID, userID, availFor, price, bhk, gender, area, parking, owner, locality, pin)
            cursor = connection.cursor()

            #fetching agent data
            Agdata = []
            agentID = str(agentID)
            cursor.execute("select Agent_ID, Name, Contact, Number_of_Properties_Sold, Number_of_Properties_Rented from agent WHERE Agent_ID = " + agentID)
            for i in cursor:
                Agdata.append(i)
            print(Agdata)    

            #cards data
            details = []
            cursor.execute("select Serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + agentID)
            for i in cursor:
                details.append(i)
            print(details) 

            # fetching serial_No count
            cursor.execute("select count(*) as count from estate")
            countSerial = []
            results = namedtuplefetchall(cursor)
            countSerial.append(results[0].count)
            print(countSerial)
            
            # updating next serial and nextAddress to one
            nextSerial = countSerial[0] + 1
            nextAddress = nextSerial
            print(nextSerial, nextAddress)

            # adding new property to the database
            # cursor.execute("INSERT into Estate Values (" + nextSerial + ", " +  agentID  + ", " +  nextAddress + ", " +  userID + ", '" + availFor + "', '" + status + "', " + price + ", " + bhk + ", '" + gender + "', " + area + ", '" + parking + "', '" + date + "', '" + owner + "')" )
            nextSerial = str(nextSerial)
            nextAddress = str(nextAddress)
            agentID = str(agentID)
            userID = str(userID)
            availFor = str(availFor)
            # status = str(status)
            price = str(price)
            bhk = str(bhk)
            gender = str(gender)
            area = str(area)
            # date = str(date)
            parking = str(parking)
            owner = str(owner)
            locality = str(locality)
            pin = str(pin)
            
            print("INSERT into Address Values (" + nextAddress + ", '" +  locality + "', " +  pin + ")")
            cursor.execute("INSERT into Address Values (" + nextAddress + ", '" +  locality + "', " +  pin + ")" )
            
            print("INSERT into Estate Values (" + nextSerial + ", " +  agentID  + ", " +  nextAddress + ", " +  userID + ", '" + availFor + "', 'Available', " + price + ", " + bhk + ", '" + gender + "', " + area + ", '" + parking + "', Null, '" + owner + "')" )
            cursor.execute("INSERT into Estate Values (" + nextSerial + ", " +  agentID  + ", " +  nextAddress + ", " +  userID + ", '" + availFor + "', 'Available', " + price + ", " + bhk + ", '" + gender + "', " + area + ", '" + parking + "', Null, '" + owner + "')" )

            #cards data
            details = []
            cursor.execute("select Serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + agentID)
            for i in cursor:
                details.append(i)
            print(details)

            #fetching agent data
            Agdata = []
            agentID = str(agentID)
            cursor.execute("select Name, agent_ID, Contact, Number_of_Properties_Sold, Number_of_Properties_Rented from agent WHERE Agent_ID = " + agentID)
            for i in cursor:
                Agdata.append(i)
            print(Agdata)

            # fetching total sale of a agent
            cursor.execute("select sum(selling_price) as total from estate where Available_for = 'Sale' and Status = 'Sold' and Agent_ID = " + agentID)
            totalSale = []
            results = namedtuplefetchall(cursor)
            totalSale.append(results[0].total)
            print(totalSale)

            data = {
                'agentName': Agdata[0][0],
                'agentID': Agdata[0][1],
                'contact': Agdata[0][2],
                'NOS': Agdata[0][3],
                'NOR': Agdata[0][4],
                'tSale': totalSale[0],
                'cardData': details
            }
            dataunique = data.copy()
            return render(request, 'realEstate/agent.html', data) 

        if 'changeStatus' in request.POST:
            change =  request.POST.get('change', '')
            a, b, c = change.split()
            print(a, b, c)
            print(change)
            print(dataunique)
            today = date.today()
            dt = today.strftime("%d-%m-%Y")
            print(dt)
            cursor = connection.cursor()
            # update estate status
            print("UPDATE Estate SET status = '" + b + "', Date_of_Sale_OR_Rent = '" + dt + "' WHERE Serial_No = " + a)
            cursor.execute("UPDATE Estate SET status = '" + b + "', Date_of_Sale_OR_Rent = '" + dt + "' WHERE Serial_No = " + a)

            ID = dataunique['agentID']
            print(ID)
            ID = str(ID)

            # update agent nos nor
            print("UPDATE agent SET Number_of_Properties_" + b + " = Number_of_Properties_" + b + " + 1 WHERE agent_ID = " + ID)
            cursor.execute("UPDATE agent SET Number_of_Properties_" + b + " = Number_of_Properties_" + b + " + 1 WHERE agent_ID = " + ID)

            print("select Serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + ID)
            cursor.execute("select Serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + ID)
            newData = []
            for i in cursor:
                newData.append(i)
            print(newData)  

            dataunique['cardData'] = newData.copy() 
            if b == 'Sold':
                dataunique['NOS'] += 1
                # dataunique['tSale'] += int(c)
                if dataunique['tSale'] is None :
                    dataunique['tSale'] = c
                else:
                    dataunique['tSale'] += int(c)
            elif b == 'Rented':
                dataunique['NOR'] += 1    
            print(dataunique) 
            
            return render(request, 'realEstate/agent.html', dataunique)
    else:
        print("when reload")
        print(dataunique)      
        return render(request, 'realEstate/agent.html', dataunique)   

def Login(request):
    global dataunique
    if request.method == "POST":
        if 'Login_admin' in request.POST:
            user = request.POST.get('email', '')
            password = request.POST.get('pass', '')
            print(user, password)
            user = str(user)
            password = str(password)

            #taking userID, category and password from database
            userIDS = []
            cursor = connection.cursor()
            cursor.execute("select User_ID, category, password from users")
            for i in cursor:
                userIDS.append(i)
            print(userIDS)

            #checking whether the id, password is true
            flag = 0
            correct = 0
            for u, c, p in userIDS:
                u = str(u)
                if u == user and c == 'Admin' and p == password:
                    flag = 1
                    break
            if flag == 1:
                correct = 1

            if correct == 1:                
                return render(request, 'realEstate/admin.html')
            else:
                return render(request, 'realEstate/index.html')

        elif 'Login_agent' in request.POST:
            user = request.POST.get('email', '')
            password = request.POST.get('pass', '')
            print(user, password)
            user = str(user)
            password = str(password)
            cursor = connection.cursor()

            #taking userID, category and password from database
            userIDS = []
            cursor = connection.cursor()
            cursor.execute("select User_ID, category, password from users")
            for i in cursor:
                userIDS.append(i)
            print(userIDS)

            #checking whether the id, password is true
            flag = 0
            correct = 0
            for u, c, p in userIDS:
                u = str(u)
                if u == user and c == 'Agent' and p == password:
                    flag = 1
                    break
            if flag == 1:
                correct = 1


            if correct == 1:
                lis = []    
                cursor.execute("Select distinct(agent.Name), agent.Agent_ID, agent.Contact, Number_of_Properties_Sold, Number_of_properties_rented from agent WHERE User_ID =  " + user)
                for i in cursor:
                    lis.append(i)
                print(lis)

                #cards data
                details = []
                UID = lis[0][1]
                UID = str(UID)
                cursor.execute("select Serial_No, selling_price, Plot_area, BHK, Parking_Available, Owner, Status, Available_For, Name, type, locality from estate,address, agent where Agent.agent_ID = Estate.agent_ID AND address.address_No = Estate.address_No AND Agent.agent_ID = " + UID)
                for i in cursor:
                    details.append(i)
                print(details) 

                # fetching total sale of a agent
                cursor.execute("select sum(selling_price) as total from estate where Available_for = 'Sale' and Status = 'Sold' and Agent_ID = " + UID)
                totalSale = []
                results = namedtuplefetchall(cursor)
                totalSale.append(results[0].total)
                print(totalSale)

                data = {
                    'agentName': lis[0][0],
                    'agentID': lis[0][1], 
                    'contact': lis[0][2],
                    'NOS': lis[0][3],
                    'NOR': lis[0][4],
                    'tSale': totalSale[0],
                    'cardData': details
                }
                dataunique = data.copy()
                return render(request, 'realEstate/agent.html', data)

            else:
                return render(request, 'realEstate/index.html')  

        elif 'Login_buyer' in request.POST:
            user = request.POST.get('email', '')
            password = request.POST.get('pass', '')
            print(user, password)
            user = str(user)
            password = str(password)

            #taking userID, category and password from database
            userIDS = []
            cursor = connection.cursor()
            cursor.execute("select User_ID, category, password from users")
            for i in cursor:
                userIDS.append(i)
            print(userIDS)

            #checking whether the id, password is true
            flag = 0
            correct = 0
            for u, c, p in userIDS:
                u = str(u)
                if u == user and c == 'Buyer' and p == password:
                    flag = 1
                    break
            if flag == 1:
                correct = 1

            if correct == 1:                
                return render(request, 'realEstate/Buyer.html')
            else:
                return render(request, 'realEstate/index.html')  
    else:        
        return render(request, 'realEstate/index.html')               

def Registration(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        userID = request.POST.get('userID', '')
        contact = request.POST.get('contact', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')
        print(name, userID, contact, password, confirm)

        #adding buyer to the database
        cursor = connection.cursor()
        print("INSERT into users Values (" + userID + ", '" + name + "', " + contact + ", 'Buyer', '" + password + "')")
        cursor.execute("INSERT into users Values (" + userID + ", '" + name + "', " + contact + ", 'Buyer', '" + password + "')")
        return render(request, 'realEstate/registration.html')
    else:    
        return render(request, 'realEstate/registration.html')  

def addAgent(request):
    if request.method == "POST":
        agentName = request.POST.get('agentName', '')
        userID = request.POST.get('userID', '')
        agentID = request.POST.get('agentID', '')
        contact = request.POST.get('contact', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')
        print(agentName, userID, agentID, contact, password, confirm)

        #adding agent to both tables(users, agent) in the database
        cursor = connection.cursor()
        agentName = str(agentName)
        userID = str(userID)
        agentID = str(agentID)
        contact = str(contact)
        password = str(password)
        confirm = str(confirm)
        print("INSERT into users Values (" + userID + ", '" + agentName + "', " + contact + ", 'Agent', '" + password + "')")
        print("INSERT into agent Values (" + agentID + ", '" + agentName + "', " + contact + ", 0, 0, " + userID + ")" )
        cursor.execute("INSERT into users Values (" + userID + ", '" + agentName + "', " + contact + ", 'Agent', '" + password + "')")
        cursor.execute("INSERT into agent Values (" + agentID + ", '" + agentName + "', " + contact + ", 0, 0, " + userID + ")" )

        return render(request, 'realEstate/addAgent.html')
    else:    
        return render(request, 'realEstate/addAgent.html')                
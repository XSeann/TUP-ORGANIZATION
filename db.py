tup_accounts =  [   {'email': 'john.doe@tup.edu.ph', 'Student No.' : 'TUPM-23-0000', 'Surname' : 'Doe', 'Firstname' : 'John', 'Sex' : 'Male', 'Year' : '1'},
                    {'email': 'sam.perez@tup.edu.ph', 'Student No.' : 'TUPM-23-2020', 'Surname' : 'Perez', 'Firstname' : 'Sam', 'Sex' : 'Male','Year' : '1'},
                    {'email': 'jane.munoz@tup.edu.ph', 'Student No.' : 'TUPM-23-2021', 'Surname' : 'Munoz', 'Firstname' : 'Jane', 'Sex' : 'Female', 'Year' : '1'},
                    {'email': 'luis.pascual@tup.edu.ph', 'Student No.' : 'TUPM-23-2018', 'Surname' : 'Pascual', 'Firstname' : 'Luis', 'Sex' : 'Male','Year' : '1'},
                    {'email': 'aaron.valdez@tup.edu.ph', 'Student No.' : 'TUPM-23-2000', 'Surname' : 'Valdez', 'Firstname' : 'Aaron', 'Sex' : 'Male','Year' : '1'},
                    {'email': 'maria.dalisay@tup.edu.ph', 'Student No.' : 'TUPM-23-2050', 'Surname' : 'Dalisay', 'Firstname' : 'Maria', 'Sex' : 'Female', 'Year' : '1'},
                    {'email': 'jana.domingo@tup.edu.ph', 'Student No.' : 'TUPM-23-2024', 'Surname' : 'Domingo', 'Firstname' : 'Jana', 'Sex' : 'Female', 'Year' : '1'},
                    {'email': 'piolo.cruz@tup.edu.ph', 'Student No.' : 'TUPM-23-2025', 'Surname' : 'Cruz', 'Firstname' : 'Piolo', 'Sex' : 'Male', 'Year' : '1'},
                    {'email': 'billy.rolex@tup.edu.ph', 'Student No.' : 'TUPM-23-2026', 'Surname' : 'Rolex', 'Firstname' : 'Billy', 'Sex' : 'Male', 'Year' : '1'},
                    {'email': 'nathan.reyes@tup.edu.ph', 'Student No.' : 'TUPM-23-2027', 'Surname' : 'Reyes', 'Firstname' : 'Nathan', 'Sex' : 'Male', 'Year' : '1'},
                    {'email': 'nina.sawyer@tup.edu.ph', 'Student No.' : 'TUPM-23-2028', 'Surname' : 'Sawyer', 'Firstname' : 'Nina', 'Sex' : 'Female', 'Year' : '1'}
                ] # TUP Accounts of Students

# LINKED LIST

class boltup_linked:
    def __init__(self, data):
        self.data = data
        self.next = None

boltup_members = {}
boltup_members['mem'] = boltup_linked(0)

class cyc_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
cyc_members = {}
cyc_members['mem'] = cyc_linked(0)

class gdg_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
gdg_members = {}
gdg_members['mem'] = gdg_linked(0)

class kpl_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
kpl_members = {}
kpl_members['mem'] = kpl_linked(0)

class osesh_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
osesh_members = {}
osesh_members['mem'] = osesh_linked(0)

class smers_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
smers_members = {}
smers_members['mem'] = smers_linked(0)

class stup_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
stup_members = {}
stup_members['mem'] = stup_linked(0)

class tupivc_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupivc_members = {}
tupivc_members['mem'] = tupivc_linked(0)

class tuppaw_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tuppaw_members = {}
tuppaw_members['mem'] = tuppaw_linked(0)

class tupdb_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupdb_members = {}
tupdb_members['mem'] = tupdb_linked(0)

class tupgear_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupgear_members = {}
tupgear_members['mem'] = tupgear_linked(0)

class tupgb_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupgb_members = {}
tupgb_members['mem'] = tupgb_linked(0)

class tupmrc_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupmrc_members = {}
tupmrc_members['mem'] = tupmrc_linked(0)

class tuptg_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tuptg_members = {}
tuptg_members['mem'] = tuptg_linked(0)

class tupdost_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
tupdost_members = {}
tupdost_members['mem'] = tupdost_linked(0)

class wbcc_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
wbcc_members = {}
wbcc_members['mem'] = wbcc_linked(0)

class yegd_linked:
    def __init__(self, data):
        self.data = data
        self.next = None
        
yegd_members = {}
yegd_members['mem'] = yegd_linked(0)

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def getOnlyData(head):
    arrayData = []
    currentNode = head
    while currentNode:
        arrayData.append(currentNode.data)
        currentNode = currentNode.next
    return arrayData

def insertNodeAtPosition(head, newNode, position):
    currentNode = head
    for i in range(position):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def deleteSpecificNode(head, nodeEmail):

    if head.data['email'] == nodeEmail:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next.data['email'] != nodeEmail:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

def count_nodes(head):

    # Counts number of nodes in linked list
    # Initialize count with 0
    count = 0

    # Initialize curr with head of Linked List
    curr = head

    # Traverse till we reach None
    while curr is not None:
        # Increment count by 1
        count += 1

        # Move pointer to next node
        curr = curr.next

    # Return the count of nodes
    return count
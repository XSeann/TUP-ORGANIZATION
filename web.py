from flask import url_for, redirect, render_template, Flask, flash, request
import orgCollection
import db

app = Flask(__name__)

app.secret_key = 'hahaha'

ORG_LISTS = ['BOLTUP', 'CYC', 'GDG', 'KPL', 'OSESH', 'SMERS', 'STUP', 'TUPIVC', 'TUPPAW', 'TUPDB', 'TUPGEAR', 'TUPGB', 'TUPMRC', 'TUPTG', 'TUPDOST', 'WBCC', 'YEGD']

LinkedOrgs = [db.boltup_linked, db.cyc_linked, db.gdg_linked, db.kpl_linked, db.osesh_linked, db.smers_linked, db.stup_linked, db.tupivc_linked, db.tuppaw_linked, db.tupdb_linked, db.tupgear_linked, db.tupgb_linked, db.tupmrc_linked, db.tuptg_linked, db.tupdost_linked, db.wbcc_linked, db.yegd_linked]

LinkedOrgMemCollection = [db.boltup_members, db.cyc_members, db.gdg_members, db.kpl_members, db.osesh_members, db.smers_members, db.stup_members, db.tupivc_members, db.tuppaw_members, db.tupdb_members, db.tupgear_members, db.tupgb_members, db.tupmrc_members, db.tuptg_members, db.tupdost_members, db.wbcc_members, db.yegd_members]

OrgPageTemplate = [orgCollection.BOLTUP, orgCollection.CYC, orgCollection.GDG, orgCollection.KPL, orgCollection.OSESH, orgCollection.SMERS, orgCollection.STUP, orgCollection.TUPIVC, orgCollection.TUPPAW, orgCollection.TUPDB, orgCollection.TUPGEAR, orgCollection.TUPGB, orgCollection.TUPMRC, orgCollection.TUPTG, orgCollection.TUPDOST, orgCollection.WBCC, orgCollection.YEGD]

tup_admin = ['boltup@tup.edu.ph', 'cyc@tup.edu.ph', 'gdg@tup.edu.ph', 'kpl@tup.edu.ph', 'osesh@tup.edu.ph', 'smers@tup.edu.ph', 'stup@tup.edu.ph'
             , 'tupivc@tup.edu.ph', 'tuppaw@tup.edu.ph', 'tupdb@tup.edu.ph', 'tupgear@tup.edu.ph', 'tupgb@tup.edu.ph', 'tupmrc@tup.edu.ph', 'tuptg@tup.edu.ph'
             , 'tupdost@tup.edu.ph', 'wbcc@tup.edu.ph', 'yegd@tup.edu.ph'] # TUP Admin that will review TUP Student Applications

tup_log = '' # TUP Email that tried to Log In

tup_stud_info = {} # TUP Student Info After Authentication

tup_auth_admin = False

tup_auth_stud = False

tup_err = False

approve = '' # TUP Admin approved the application for organization

deny = '' # TUP Admin denied the application for organization

class Stack:
    def __init__(self):
        self.ORG_STACKS = []
        # TUP Students Messages that will be stored on their respective Organization
        for pos in range(len(ORG_LISTS)):
            self.ORG_STACKS.append({ORG_LISTS[pos] : []})
    
    def push(self, element):
        for pos in range(len(ORG_LISTS)):
            if element['org'] == ORG_LISTS[pos]:
                self.ORG_STACKS[pos][ORG_LISTS[pos]].append(element)
    
    def pop(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return self.ORG_STACKS[pos][ORG_LISTS[pos]].pop()
    
    def peek(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                if self.isEmpty(ORG_LISTS[pos]):
                    return "Stack is empty"
                return self.ORG_STACKS[pos][ORG_LISTS[pos]][0]
    
    def isEmpty(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return len(self.ORG_STACKS[pos][ORG_LISTS[pos]]) == 0
        
    def size(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return len(self.ORG_STACKS[pos][ORG_LISTS[pos]])

# Create a stack
myStack = Stack()

myStack.push({'email': 'jana.domingo@tup.edu.ph', 'Student No.' : 'TUPM-23-2024', 'Surname' : 'Domingo', 'Firstname' : 'Jana', 'Sex' : 'Female', 'Year' : '1', 'org': 'BOLTUP', 'mes': 'Hello HelloHelloHelloHelloHello Hello Hello Hello HelloHelloHello Hello Hello Hello Hello Hello HelloHelloHelloHelloHello Hello Hello Hello HelloHelloHello Hello Hello Hello Hello Hello HelloHelloHelloHelloHello Hello Hello Hello HelloHelloHello Hello Hello Hello Hello Hello'})
myStack.push({'email': 'piolo.cruz@tup.edu.ph', 'Student No.' : 'TUPM-23-2025', 'Surname' : 'Cruz', 'Firstname' : 'Piolo', 'Sex' : 'Male', 'Year' : '1', 'org': 'CYC', 'mes': 'jasjbjabd'})
myStack.push({'email': 'billy.rolex@tup.edu.ph', 'Student No.' : 'TUPM-23-2026', 'Surname' : 'Rolex', 'Firstname' : 'Billy', 'Sex' : 'Male', 'Year' : '1', 'org': 'TUPPAW', 'mes': 'kanslknkanksdl'})
myStack.push({'email': 'nathan.reyes@tup.edu.ph', 'Student No.' : 'TUPM-23-2027', 'Surname' : 'Reyes', 'Firstname' : 'Nathan', 'Sex' : 'Male', 'Year' : '1', 'org': 'BOLTUP', 'mes': 'Hi'})
myStack.push({'email': 'nina.sawyer@tup.edu.ph', 'Student No.' : 'TUPM-23-2028', 'Surname' : 'Sawyer', 'Firstname' : 'Nina', 'Sex' : 'Female', 'Year' : '1', 'org': 'TUPIVC', 'mes': 'zxocozxckkj'})

class Queue:
    def __init__(self):
        self.ORG_QUEUES = []
        for pos in range(len(ORG_LISTS)):
            self.ORG_QUEUES.append({ORG_LISTS[pos] : []})
        self.boltup_queues = []
    
    def enqueue(self, element):
        for pos in range(len(ORG_LISTS)):
            if element['org'] == ORG_LISTS[pos]:
                self.ORG_QUEUES[pos][ORG_LISTS[pos]].append(element)
    
    def dequeue(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return self.ORG_QUEUES[pos][ORG_LISTS[pos]].pop(0)
    
    def peek(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                if self.isEmpty(ORG_LISTS[pos]):
                    return print('QUEUE IS EMPTY')
                return self.ORG_QUEUES[pos][ORG_LISTS[pos]][0]
    
    def isEmpty(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return len(self.ORG_QUEUES[pos][ORG_LISTS[pos]]) == 0
    
    def size(self, org):
        for pos in range(len(ORG_LISTS)):
            if org == ORG_LISTS[pos]:
                return len(self.ORG_QUEUES[pos][ORG_LISTS[pos]])

# Create a queue
myQueue = Queue()

#myQueue.enqueue({'email': 'sam.perez@tup.edu.ph', 'Student No.' : 'TUPM-23-2020', 'Surname' : 'Perez', 'Firstname' : 'Sam', 'Sex' : 'Male', 'Year' : '1', 'org': 'TUPTG'})
myQueue.enqueue({'email': 'jane.munoz@tup.edu.ph', 'Student No.' : 'TUPM-23-2021', 'Surname' : 'Munoz', 'Firstname' : 'Jane', 'Sex' : 'Female', 'Year' : '1', 'org': 'CYC'})
myQueue.enqueue({'email': 'luis.pascual@tup.edu.ph', 'Student No.' : 'TUPM-23-2018', 'Surname' : 'Pascual', 'Firstname' : 'Luis', 'Sex' : 'Male', 'Year' : '1', 'org': 'GDG'})
myQueue.enqueue({'email': 'aaron.valdez@tup.edu.ph', 'Student No.' : 'TUPM-23-2000', 'Surname' : 'Valdez', 'Firstname' : 'Aaron', 'Sex' : 'Male', 'Year' : '1', 'org': 'BOLTUP'})
myQueue.enqueue({'email': 'maria.dalisay@tup.edu.ph', 'Student No.' : 'TUPM-23-2050', 'Surname' : 'Dalisay', 'Firstname' : 'Maria', 'Sex' : 'Female', 'Year' : '1', 'org': 'BOLTUP'})


newMem = db.boltup_linked({'email': 'john.doe@tup.edu.ph', 'Student No.' : 'TUPM-23-0000', 'Surname' : 'Doe', 'Firstname' : 'John', 'Sex' : 'Male', 'Year' : '1', 'org' : 'BOLTUP'}) # 
db.insertNodeAtPosition(db.boltup_members['mem'], newMem, db.count_nodes(db.boltup_members['mem'])-1)

@app.route('/')
def index():
    global tup_err
    print(tup_err)
    if tup_err == True:
        
        flash('Not A TUP Account!')

    return render_template('index.html')

@app.route('/org', methods=['POST'])
def org():

    global tup_auth_stud

    orgType = request.form.get('orgType')

    print(orgType)

    for pos in range(len(ORG_LISTS)):
        if orgType == ORG_LISTS[pos] and tup_auth_stud == True:
            return render_template('org.html', body=orgCollection.HEAD + OrgPageTemplate[pos], withOrg=False)
    
    return redirect('/home')

@app.route('/login')
def login():
    global tup_auth_admin, tup_auth_stud

    if tup_auth_admin == False and tup_auth_stud == False: 
        return render_template('login.html')
    return redirect('/home')

@app.route('/auth', methods=['POST'])
def auth():
    global tup_log, tup_auth_admin, tup_auth_stud, tup_err, tup_stud_info

    tup_log = request.form.get('email')
    tup_err = True

    for pos in range(len(tup_admin)):
        if tup_log == tup_admin[pos]:
            tup_auth_admin = True
            tup_err = False
            return redirect('/home')
    # Linear Search to see if the email that has login is a TUP Account
    for i in range(len(db.tup_accounts)):
        if tup_log == db.tup_accounts[i]['email']:
            tup_auth_stud = True
            tup_stud_info = db.tup_accounts[i]
            tup_err = False
            return redirect('/home')
    
    return redirect('/') 

@app.route('/home')
def home():
    global tup_log, tup_auth_admin, tup_auth_stud

    def reverseStack(stack):
        arr = []

        for pos in range(len(stack)):
            arr.append(stack[pos])
        
        arr.reverse()

        return arr

    def popMany(arr, num):
        for x in range(num):
            arr.pop()
        return arr

    for pos in range(len(ORG_LISTS)):
        if tup_auth_admin == True and tup_log == tup_admin[pos]:
            return render_template('homeAdmin.html', apply=myQueue.ORG_QUEUES[pos][ORG_LISTS[pos]], applicantsLength=myQueue.size(ORG_LISTS[pos]), member=db.getOnlyData(LinkedOrgMemCollection[pos]['mem'].next), membersLength=db.count_nodes(LinkedOrgMemCollection[pos]['mem'].next), messages=reverseStack(myStack.ORG_STACKS[pos][ORG_LISTS[pos]]), messagesLength=myStack.size(ORG_LISTS[pos]))
    
    if tup_auth_stud == True:
        for pos in range(len(ORG_LISTS)):
            Members = db.getOnlyData(LinkedOrgMemCollection[pos]['mem'].next)
            for pos2 in range(len(Members)):
                if tup_log == Members[pos2]['email']:
                    return render_template('homeStudent.html', org=orgCollection.HEAD + '\n'.join(popMany(OrgPageTemplate[pos2].split('\n'), 6)), withOrg=True)
            for pos2 in range(myQueue.size(ORG_LISTS[pos])):
                if tup_log == myQueue.ORG_QUEUES[pos][ORG_LISTS[pos]][pos2]['email']:
                    return render_template('homeStudent.html', inQueue=True)
        return render_template('homeStudent.html', withOrg=False)
    
    return redirect('/')

@app.route('/apply', methods=['POST'])
def apply():
    global tup_auth_stud, tup_stud_info, approve, deny

    if tup_auth_admin == True:
        approve = request.form.get('approve') 
        deny = request.form.get('deny')

        if approve == 'Approve':
            for pos in range(len(ORG_LISTS)):
                if tup_log == tup_admin[pos]: 
                    newMem = LinkedOrgs[pos](myQueue.peek(ORG_LISTS[pos])) # 
                    db.insertNodeAtPosition(LinkedOrgMemCollection[pos]['mem'], newMem, db.count_nodes(LinkedOrgMemCollection[pos]['mem'])-1) # Student Info will be in the org linked list when accepted
                    db.traverseAndPrint(LinkedOrgMemCollection[pos]['mem'])
                    myQueue.dequeue(ORG_LISTS[pos]) # Students who are accepted will be Dequeued (Queue) from the waiting list
            approve = ''

        if deny == 'Deny':
            for pos in range(len(ORG_LISTS)):
                if tup_log == tup_admin[pos]: 
                    myQueue.dequeue(ORG_LISTS[pos]) # Students who are accepted will be Dequeued (Queue) from the waiting list
            deny= ''

    if tup_auth_stud == True:
        org = request.form.get('org')
        tup_stud_info['org'] = org # Adding another property to the student info when Student applied to an org
        myQueue.enqueue(tup_stud_info) # Student Info will be Enqueued (Queue) when they had applied to an org
        flash("Successful")
        return redirect(url_for('org'), code=307)
        
    return redirect('/home')

@app.route('/remove', methods=['POST'])
def remove():
    global tup_auth_admin

    removeUser = request.form.get('removeUser')

    def deleteSpecificNode(head, nodeEmail):
        if head.data > 0:
            return head.next
        currentNode = head
        # Linear Search for TUP Student removal from a certain org
        while currentNode.next and currentNode.next.data['email'] != nodeEmail:
            currentNode = currentNode.next

        currentNode.next = currentNode.next.next

        return head
    
    print(removeUser)

    if tup_auth_admin == True:
        for pos in range(len(ORG_LISTS)):
            if tup_log == tup_admin[pos]:
                deleteSpecificNode(LinkedOrgMemCollection[pos]['mem'], removeUser)
                db.traverseAndPrint(LinkedOrgMemCollection[pos]['mem'])
                return redirect('/home')
            
    return redirect('/home')

@app.route('/sendMes', methods=['POST'])
def sendMes():
    global tup_auth_admin

    mes = request.form.get('mesToAdmin')

    if tup_auth_stud == True:
        for pos in range(len(ORG_LISTS)):
            Members = db.getOnlyData(LinkedOrgMemCollection[pos]['mem'].next)
            for pos2 in range(len(Members)):
                if tup_log == Members[pos2]['email']:
                    Members[pos]['mes'] = mes
                    print(Members)
                    myStack.push(Members[pos])

    return redirect('/home')

@app.route('/removeMes', methods=['POST'])
def removeMes():
    global tup_auth_admin

    if tup_auth_admin == True:
        for pos in range(len(ORG_LISTS)):
            if tup_log == tup_admin[pos]:
                myStack.pop(ORG_LISTS[pos]) # Stack Pop
        
    return redirect('/home')

@app.route('/sort')
def sort():
    global tup_auth_admin

    def insertionSort(arr):
        #Insertion Sort
        for pos in range(len(arr)):
            for pos2 in range(pos):
                if arr[pos]['Surname'] < arr[pos2]['Surname']:
                    arr[pos], arr[pos2] = arr[pos2], arr[pos]
        return arr
    
    def newNodeData(head, data):
        currentNode = head
        for pos in range(len(data)):
            currentNode.data = data[pos]
            currentNode = currentNode.next
    
    #Sort By Surname A-Z
    if tup_auth_admin == True:
        for pos in range(len(ORG_LISTS)):
            if tup_log == tup_admin[pos]:
                arr = db.getOnlyData(LinkedOrgMemCollection[pos]['mem'].next)
                arr = insertionSort(arr)
                newNodeData(LinkedOrgMemCollection[pos]['mem'].next, arr)
                db.traverseAndPrint(db.boltup_members['mem'])

    return redirect('/home')

@app.route('/cancel')
def cancel():
    global tup_log, tup_auth_stud

    if tup_auth_stud == True:
        for pos in range(len(ORG_LISTS)):
            InQueue = myQueue.ORG_QUEUES[pos][ORG_LISTS[pos]]
            for pos2 in range(len(InQueue)):
                if tup_log == InQueue[pos2]['email']:
                    InQueue.pop(pos2)
                    return redirect('/home')
                
    return redirect('/home')

@app.route('/logout')
def logout():
    global tup_auth_admin, tup_auth_stud, tup_stud_info, tup_log

    tup_auth_admin = tup_auth_stud = False
    tup_stud_info = {}
    tup_log = ''

    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)
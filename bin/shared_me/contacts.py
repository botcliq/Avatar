class contacts_manager(dict):
    def __init__(self, contact_list, **kwargs):
        """
        create a new contact manager, recive a contact objecat and add it to the managelist.
        :param contact:
        :return:
        """
        super(contacts_manager, self).__init__(**kwargs)
        for c in contact_list:
            self.add_contacts(c)

    def add_contacts(self,contacts):
        """
        Add a particular contact id to the contact manager
        :param contacts:
        :return:
        """
        self[contacts.id] = contacts

    def delete_contacts(self,id):
        """
        Delete the contact given with the contact id
        :param id:
        :return:
        """
        try:
            del self[id]
        except:
            print "The contact doesn't exist."

    def view_contacts(self):
        """
        view all contacts related to a profile
        :return:
        """
        return self.values()

    def view_contact(self,contact_id):
        return self[contact_id]

class contact:
    def __init__(self,id,name,emailid='',phone='',address=''):
        self.id = id
        self.name = name
        self.email = emailid
        self.phoen = phone
        self.address = address

    def set_name(self,value):
        self.name = value

    def set_email(self,emailid):
        self.email = emailid

    def set_phone(self,phone):
        self.phone = phone

    def set_address(self,address):
        self.address = address
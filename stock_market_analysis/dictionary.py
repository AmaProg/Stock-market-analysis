class Dictionary(dict):
    
    #----- constructor -----
    #----- end constructor -----
    
    #----- methods -----
    def first_value(self, external_dict: dict = {}):
        """_summary_

        Returns:
            _type_: _description_
        """
        if(len(external_dict) != 0):
            return list(external_dict.values())[0]
        
        else:
            return list(self.values())[0]
    
    def last_value(self, external_dict: dict = {}):
        """_summary_

        Returns:
            _type_: _description_
        """
        if(len(external_dict) != 0):
            number_element = len(external_dict) - 1
            return list(external_dict.values())[number_element]
        
        else:
            number_element = len(self) - 1
            return list(self.values())[number_element]
    #----- end methods -----
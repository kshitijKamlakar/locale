from typing import Any


class Create_node :

    def __init__(self,is_input_node,is_output_node,parent_node_ids,query_type,create_relation):
        self.is_input_node = is_input_node
        self.is_output_node = is_output_node
        self.parent_node_ids = parent_node_ids
        self.query_type = query_type
        self.create_relation = create_relation

    def set_input_node(self,value):
        self.is_input_node = value

    def set_output_node(self,value):
        self.is_output_node = value

    def set_parent_node_ids(self,value):
        self.parent_node_ids = value

    def set_query_type(self,value,tableName):
        self.query_type = "select trans_id,(" + value +") as A from  "+tableName
    def set_create_relation(self,value):
        self.create_relation = "select "
        self.create_relation= value

    def get_input_node(self):
        return self.is_input_node

    def get_output_node(self):
        return self.is_output_node

    def get_parent_node_ids(self):
        return self.parent_node_ids

    def get_query_type(self):
        return self.query_type

    def get_create_relation(self):

        return self.create_relation

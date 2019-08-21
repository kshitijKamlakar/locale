import random
import string
from string import  ascii_lowercase
from random import choices

from pip._vendor.distlib.compat import raw_input

from create_node import Create_node

if __name__ == '__main__':
    attribute_input_1 = raw_input("Enter the Element of table Order :")
    attribute_input_2 = raw_input("Enter the Element of table Merchent :")

    input_node_1 = Create_node(None,None,None,None,None)
    input_node_2 = Create_node(None, None, None, None, None)
    operation_node = Create_node(None, None, [input_node_1, input_node_2], None, None)
    input_node_1.set_query_type(attribute_input_1,"Order")
    input_node_2.set_query_type(attribute_input_2,"Merchant")
    input_node_1.set_output_node(operation_node)
    input_node_2.set_output_node(operation_node)
    input_node_1.set_create_relation({input_node_1: operation_node})
    input_node_2.set_create_relation({input_node_2: operation_node})
    nodeList = [input_node_1, input_node_2,operation_node]

    def getSQL(nodeList) :

        temp_alias = ""
        temp_select = ""
        where = ""
        operator = "-"
        output_query = ""
        for node in nodeList :
            if node.get_parent_node_ids() == None :
                continue
            else :
                i = 0
                for parent in node.get_parent_node_ids() :
                    temp_alias = generateLetter()
                    if i ==0 :
                        temp_select = "Select "+ temp_alias+".A  "
                        where = " where " + temp_alias+".id ="
                        from_value = "from ( " + parent.get_query_type()+" ) AS " +temp_alias
                        i = i +1
                    else :
                        temp_select = temp_select +" "+  operator  + " "+ temp_alias+".A  "
                        where = where + temp_alias + ".trans_id"
                        from_value = from_value + ", (" + parent.get_query_type() + ") AS " + temp_alias


                output_query = temp_select + from_value + where + ";"
                outputNode = Create_node([operation_node],None,[operation_node],output_query,None)
        return  outputNode.get_query_type()


    def generateLetter():
        genString = "".join(random.choice(ascii_lowercase) for x in range(random.randint(3, 3)))
        return genString


    print(getSQL(nodeList))
from models.LinkedList import LinkedList

def main():

    country_list = LinkedList()
    while True:
        list = input().split(" ")
        if list[0] == "RPI":
            country_list.insert_at_start(list[1])
            country_list.traverse_list()

        
        elif list[0] == "RPF":
            country_list.insert_at_end(list[1])
            country_list.traverse_list()
        
        elif list[0] == "RPDE":
            country_list.insert_after_item(list[2], list[1])
            country_list.traverse_list()


        elif list[0] == "RPAE":
            country_list.insert_before_item(list[2], list[1])
            country_list.traverse_list()


        elif list[0] == "RPII":
            country_list.insert_at_index(int(list[2]), list[1])
            country_list.traverse_list()

        elif list[0] == "VNE":
            country_count = country_list.get_count()
            print(f"O número de elementos são {country_count}.")

        elif list[0] == "VP":
            country_error = country_list.search_item(list[1])
            if country_error:
                print(f"O país {list[1]} encontra-se na lista.")
            else:
                print(f"O país {list[1]} não se encontra na lista.")
        

        elif list[0] == "EPE":
            country_eliminated = country_list.start_node.get_item()
            country_list.delete_at_start()
            print(f"O país {country_eliminated} foi eliminado da lista.")


        elif list[0] == "EUE":
            country_eliminated = country_list.get_last_node()
            country_list.delete_at_start()
            print(f"O país {country_eliminated} foi eliminado da lista.")


        elif list[0] == "EP":
            check_country = country_list.search_item(list[1])
            if check_country:
                country_list.delete_element_by_value(list[1])
                print(f"O país {list[1]} foi eliminado da lista.")
            else:
                print(f"O país {list[1]} não se encontra na lista.")
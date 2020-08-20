class Node:
    def __init__(self, year, highlight, next_node=None):
        self.year = year
        self.highlight = highlight
        self.next_node = next_node

    def get_year(self):
        return self.year

    def get_highlight(self):
        return self.highlight

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, year=None, highlight=None):
        self.head_node = Node(year, highlight)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_year, new_highlight):
        new_node = Node(new_year, new_highlight)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # def insert(self, new_year, new_highlight):
    #     new_node = Node(new_year, new_highlight)
    #     current_node = self.get_head_node()
    #     if current_node.get_year() > new_year:
    #         new_node.set_next_node(self.head_node)
    #         self.head_node = new_node
    #     else:
    #         while current_node:
    #             if current_node.get_next_node() is None:
    #                 break
    #             else:
    #                 next_node = current_node.get_next_node()
    #             if next_node.get_year() > new_year:
    #                 current_node.set_next_node(new_node)
    #                 new_node.set_next_node(next_node)
    #                 current_node = new_node.get_next_node()
    #             else:
    #                 current_node = next_node

    # def get_all_years(self):
        # years_list = []
        # current_node = self.get_head_node()
        # while current_node:
        #     years_list.append(current_node.get_year())
        #     current_node = current_node.get_next_node()
        # return years_list

    def get_data(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_year() is not None:
                string_list += "Year: " + \
                               str(current_node.get_year()) + ", highlight: " + current_node.get_highlight() + "\n"
            current_node = current_node.get_next_node()
        return string_list


h = LinkedList(7, "I turned seven")
h.insert_beginning(3, "I started walking")
h.insert_beginning(1, "I was born")

current_node = h.get_head_node()
age = int(input("What's your age? "))

while current_node.get_year() < age:
    current_age = current_node.get_year() +1
    if current_node.get_next_node() is not None and current_node.get_next_node().get_year() == current_age:
        current_node = current_node.get_next_node()
    else:
        summary = input("What's your highlight of age "+ str(current_age)+"? ")
        new_node = Node(current_age, summary, current_node.get_next_node())
        current_node.set_next_node(new_node)
        current_node = new_node

print(h.get_data())
# print(h.get_data())
# print(h.get_all_years())
# all_years = h.get_all_years()
# for i in range(8):
#     if i + 1 in all_years:
#         continue
#     else:
#         summary = input("Enter the highlight of " + str(i + 1) + ": ")
#         h.insert(i + 1, summary)


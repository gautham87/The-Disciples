to_do_list = {}
def delete_item_from_to_do_list(task_to_delete):
    del to_do_list[task_to_delete]


def update_to_do_list(task_to_update):
    to_do_list[task_to_update] = "complete"
    print('Task has been Updated to complete')

def add_to_to_do_list(task):
    to_do_list[task]= 'incomplete'
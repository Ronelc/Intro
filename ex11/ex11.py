################################################################
# FILE :ex11.py
# WRITER : ronel_charedim , ronelharedim , 208917641
# EXERCISE : intro2cs2 ex11 2020
# DESCRIPTION: Trees exercise
#################################################################
import itertools

class Node:
    """
    A class that represents each node object ( that is a node in a tree ).
    """

    def __init__(self, data, positive_child=None, negative_child=None):
        """
        A constructor for a Node object
        :param data: string value. If the Node is not leaf, it represents the
                    question asked at this node. But if the Node is a
                    leaf, it represents the decision indicated by this leaf.
        :param positive_child: If the node is a leaf, it represents the node that matches
                    a positive answer to the question. But if the Node is a
                    leaf, it is None.
        :param negative_child: If the node is a leaf, it represents the node that matches
                    a negative answer to the question. But if the Node is a
                    leaf, it is None.
        """
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

class Record:
    """
    A class that represents records ( illness and list of symptoms )
    """

    def __init__(self, illness, symptoms):
        """
        A constructor for a Record Class
        :param illness: string of one illness
        :param symptoms: list of possibles symptoms. Can be empty.
        """
        self.illness = illness
        self.symptoms = symptoms

def parse_data(filepath):
    """
    This function transforms the filepath to a list of record objects.
    :param filepath: file to open
    :return: list with string of the illness and list of symptoms.
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records

class Diagnoser:
    """
    A class that represents diagnoses ( that finds illness from symptoms )
    """

    def __init__(self, root):
        """
        A constructor for a Diagnoser class
        :param root: node that represents the root of one tree. It has 2 sons.
        """
        self.root = root

    def diagnose(self, symptoms):
        """
        Function who gets a list of symptoms and diagnoses which disease is right
        for them according to the decision tree in self
        :param symptoms: list of smptoms.
        :return: The disease found on the leaf that reached it
        """
        step = self.root
        while step.negative_child != None and step.positive_child != None:
            if step.data in symptoms:
                step = step.positive_child
            else:
                step = step.negative_child
        return step.data

    def calculate_success_rate(self, records):
        """
        This function returns the fraction between the number of times the
        correct illness has been received in the total number of records.
        :param records: List of Record objects
        :return: The result
        """
        total = len(records)
        counter = 0
        for record in records:
            illness = record.illness
            symptoms = record.symptoms
            outcome = self.diagnose(symptoms)
            if outcome == illness:
                counter += 1
        return counter / total

    def helper_all_illness(self, step, illness_dict):
        """
        this function finds all the leaf ( so the illnesses ) of the tree. One
        leaf is a node that hasn't child.
        :param step: the tree root
        :param dic_illness:  A dictionary that saves all diseases with
               the number of times they appeared in the tree
        :return: illness dictionary
        """
        if step.positive_child == None and step.positive_child == None:
            if step.data not in illness_dict.keys():
                illness_dict[step.data] = 1
            else:
                illness_dict[step.data] += 1
            return
        else:
            self.helper_all_illness(step.positive_child, illness_dict)
            self.helper_all_illness(step.negative_child, illness_dict)
        return illness_dict

    def all_illnesses(self):
        """
        A function that sorts the diseases by the number of
        times they appear in the tree
        :return: sorted list
        """
        root = self.root
        dict = self.helper_all_illness(root, {})
        sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
        lst = []
        for tup in sorted_dict[::-1]:
            lst.append(tup[0])
        return lst

    def helper_paths_to_illness(self, step, illness, lst, final_lst):
        """
        this function tries all the paths that exists with the backtracking
        method and adds the good path(s) ( those which achieve the illness )
        in the final list.
        :param step: the tree root
        :param illness: illness
        :param lst: empty list
        :param finle_lst: empty list
        """
        if step.positive_child == None and step.positive_child == None:
            if step.data == illness:
                final_lst.append(lst)
        else:
            self.helper_paths_to_illness(step.positive_child, illness,
                                         lst + [True], final_lst)
            self.helper_paths_to_illness(step.negative_child, illness,
                                         lst + [False], final_lst)

    def paths_to_illness(self, illness):
        """
        this function tries all the paths that exists with the backtracking
        method and adds the good path(s) ( those which achieve the illness )
        in the final list.
        :param illness: illness
        :return: list of all paths
        """
        lst = []
        self.helper_paths_to_illness(self.root, illness, [], lst)
        return lst

def help_build(symptoms):
    """
    A function that builds a tree according to the list of symptoms
    :param symptoms: list of symptoms.
    :return: a tree
    """
    if len(symptoms) == 0:
        return Node(None)
    tree = Node(symptoms[0], help_build(symptoms[1:]),
                help_build(symptoms[1:]))
    return tree

def find_ill(records, path, symptoms):
    """
    A function that finds the illness most appropriate
    :param records: List of Record objects
    :param path: path to the illness
    :param symptoms: list of symptoms.
    :return: The most appropriate illness
    """
    dict = {}
    for record in records:
        lst = []
        for symptom in symptoms:
            q = symptom in record.symptoms
            lst.append(q)
        if lst == path:
            if record.illness in dict.keys():
                dict[record.illness] += 1
                continue
            dict[record.illness] = 1
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    if len(sorted_dict) == 0:
        return None
    return sorted_dict[-1][0]


def push(tree, path, illness):
    """
    A function that updates the leaf to be the most appropriate illness
    :param tree: tree root
    :param path: path to the illness
    :param illness: The most appropriate illness
    """
    step = tree
    i = 0
    while step.data != None:
        if path[i]:
            i += 1
            step = step.positive_child
            continue
        i += 1
        step = step.negative_child
    step.data = illness

def build_tree(records, symptoms):
    """
    A function that builds a tree as required
    :param records: list of objects of "Record" class
    :param symptoms: symptoms list
    :return: tree
    """
    tree = help_build(symptoms)
    root = Diagnoser(tree)
    paths = root.paths_to_illness(None)
    for path in paths:
        illness = find_ill(records, path, symptoms)
        push(tree, path, illness)
    return tree



def optimal_tree(records, symptoms, depth):
    """
    This function returns the tree whose diagnoses are the most efficient
    between all the possible trees that we can create with all the combinations
    of symptoms.
    :param records: List of Record objects
    :param symptoms: list of symptoms
    :param depth: Size of a subset of symptoms
    :return: The tree with the highest success rates
    """
    symptoms_sub_lst = []
    dict = {}
    for lst in (itertools.combinations(symptoms, depth)):
        symptoms_sub_lst.append(list(lst))
    for sub in symptoms_sub_lst:
        tree = build_tree(records, sub)
        calculate = Diagnoser(tree).calculate_success_rate(records)
        dict[tree] = calculate
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    return sorted_dict[-1][0]


if __name__ == "__main__":
    pass

import matplotlib.pyplot as plt

# returns a list with the elements that are in the first list and not the second one
def in_first_list_and_not_second(first_list, second_list):
    to_return = []
    for name in first_list:
        if name not in second_list:
            to_return.append(name)
    return to_return


# prints lines and conditions graphs
def plot_both_amounts_graphs(results, save_name):
    plot_amounts_graph(results, save_name, True)
    plot_amounts_graph(results, save_name, False)



# plot a graph of function lines number to condition number.
def plot_amounts_graph(results, save_name, is_lines):
    if is_lines:
        counter_type = '_lines'
        column = 2
    else:
        counter_type = '_conditions'
        column = 3
    y_axis = list(map(int, column_from_2dim_list(results, column)))

    counters = []
    for i in range(max(y_axis) + 1):
        counters.append(y_axis.count(i))

    plt.plot(range(max(y_axis) + 1), counters, 'b.')
    plt.xlabel(counter_type[1:] + ' num')
    plt.ylabel('amount')

    plt.savefig('/mnt/c/TransCoder/outputs/figs/' + save_name + counter_type + '.png')
    plt.close()

# organizes line from file
def organize_line(line):
    splitted = line.split()
    return splitted[0], splitted[6], splitted[2], splitted[4]


def column_from_2dim_list(two_dim_list, column):
    return list(map(lambda line: line[column], two_dim_list))

if __name__ == '__main__':
    no_slice_path = '/mnt/c/TransCoder/outputs/no_slices_run/tests_run_check_java.txt'
    slice_path = '/mnt/c/TransCoder/outputs/slices_run/tests_run_check_java.txt'

    # get data from files
    with open(no_slice_path) as no_slices_file:
        no_slices_lines = no_slices_file.readlines()
    with open(slice_path) as slices_file:
        slices_lines = slices_file.readlines()

    # clean data to only results
    no_slices_results = list(map(organize_line, no_slices_lines))
    slices_results = list(map(organize_line, slices_lines))

    # filter to the different kinds:
    # -1 - did not run (or infinite loop)
    # 10 - perfect run - all tests are successes
    # anything else - ran but with mistakes
    no_slices_perfect_results = list(filter(lambda line: line[1] == '10', no_slices_results))
    no_slices_not_run_results = list(filter(lambda line: line[1] == '-1', no_slices_results))
    no_slices_medium_results = list(filter(lambda line: line[1] != '-1' and line[1] != '10', no_slices_results))
    slices_perfect_results = list(filter(lambda line: line[1] == '10', slices_results))
    slices_not_run_results = list(filter(lambda line: line[1] == '-1', slices_results))
    slices_medium_results = list(filter(lambda line: line[1] != '-1' and line[1] != '10', slices_results))


    # plot graphs that shows us functions length and conditions num to successes
    plot_both_amounts_graphs(no_slices_perfect_results, 'no_slices_perfect_results')
    plot_both_amounts_graphs(no_slices_not_run_results, 'no_slices_not_run_results')
    plot_both_amounts_graphs(no_slices_medium_results, 'no_slices_medium_results')
    plot_both_amounts_graphs(slices_perfect_results, 'slices_perfect_results')
    plot_both_amounts_graphs(slices_not_run_results, 'slices_not_run_results')
    plot_both_amounts_graphs(slices_medium_results, 'slices_medium_results')


    # stay with the names
    no_slices_perfect_names = column_from_2dim_list(no_slices_perfect_results, 0)
    no_slices_not_run_names = column_from_2dim_list(no_slices_not_run_results, 0)
    slices_perfect_names = column_from_2dim_list(slices_perfect_results, 0)
    slices_not_run_names = column_from_2dim_list(slices_not_run_results, 0)

    # find differences
    slices_added_perfect = in_first_list_and_not_second(slices_perfect_names, no_slices_perfect_names)
    slices_destroyed_perfect = in_first_list_and_not_second(no_slices_perfect_names, slices_perfect_names)

    slices_added_no_run = in_first_list_and_not_second(slices_not_run_names, no_slices_not_run_names)
    slices_destroyed_no_run = in_first_list_and_not_second(no_slices_not_run_names, slices_not_run_names)

    with open('/mnt/c/TransCoder/outputs/comparison.txt', 'w') as comparison:
        comparison.write('added perfect: \n\n')
        comparison.write('\n'.join(slices_added_perfect))
        comparison.write('\n\nadded no run: \n\n')
        comparison.write('\n'.join(slices_added_no_run))

        comparison.write('\n\ndestroyed perfect: \n\n')
        comparison.write('\n'.join(slices_destroyed_perfect))
        comparison.write('\n\ndestroyed no run: \n\n')
        comparison.write('\n'.join(slices_destroyed_no_run))

# returns a list with the elements that are in the first list and not the second one
def in_first_list_and_not_second(first_list, second_list):
    to_return = []
    for name in first_list:
        if name not in second_list:
            to_return.append(name)
    return to_return

if __name__ == '__main__':
    no_slice_path = '/mnt/c/TransCoder/outputs/no_slices_run/tests_run_check_java.txt'
    slice_path = '/mnt/c/TransCoder/outputs/slices_run/tests_run_check_java.txt'

    # get data from files
    with open(no_slice_path) as no_slices_file:
        no_slices_lines = no_slices_file.readlines()
    with open(slice_path) as slices_file:
        slices_lines = slices_file.readlines()

    # clean data to only results
    no_slices_results = list(map(lambda line: (line.split()[0], line.split()[6]), no_slices_lines))
    slices_results = list(map(lambda line: (line.split()[0], line.split()[6]), slices_lines))

    # filter to perfect and didnt run
    no_slices_perfect = list(map(lambda line: line[0], filter(lambda line: line[1] == '10', no_slices_results)))
    no_slices_not_run = list(map(lambda line: line[0],filter(lambda line: line[1] == '-1', no_slices_results)))
    slices_perfect = list(map(lambda line: line[0],filter(lambda line: line[1] == '10', slices_results)))
    slices_not_run = list(map(lambda line: line[0],filter(lambda line: line[1] == '-1', slices_results)))

    # find differences
    slices_added_perfect = in_first_list_and_not_second(slices_perfect, no_slices_perfect)
    slices_destroyed_perfect = in_first_list_and_not_second(no_slices_perfect, slices_perfect)

    slices_added_no_run = in_first_list_and_not_second(slices_not_run, no_slices_not_run)
    slices_destroyed_no_run = in_first_list_and_not_second(no_slices_not_run, slices_not_run)

    with open('/mnt/c/TransCoder/outputs/comparison.txt', 'w') as comparison:
        comparison.write('added perfect: \n\n')
        comparison.write('\n'.join(slices_added_perfect))
        comparison.write('\n\nadded no run: \n\n')
        comparison.write('\n'.join(slices_added_no_run))

        comparison.write('\n\ndestroyed perfect: \n\n')
        comparison.write('\n'.join(slices_destroyed_perfect))
        comparison.write('\n\ndestroyed no run: \n\n')
        comparison.write('\n'.join(slices_destroyed_no_run))
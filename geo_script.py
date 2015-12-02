import sys  # Used to get the filename to reverse-geocode
import csv  # Used to traverse the csv file
import geocoder  # Used as the main reverse-geocoding algorithm

def rev_geocode(latitude, longitude):
    ret = geocoder.google([latitude, longitude], method='reverse')
    return ret


def traverse_csv(filename):
    print('Reverse geocoding coordinates... Please Wait.....')
    with open(filename,'rw') as csvfile:
        with open('output.csv','w') as csvoutput:
            csv_reader = csv.reader(csvfile, delimiter=',')
            csv_writer = csv.writer(csvoutput, lineterminator='\n')
            row_counter=1
            for row in csv_reader:
                #geocoding coordinates
                print('*' * 100)
                print('geocoding row:' + str(row_counter))
                row.append(rev_geocode(row[4],row[5]))
                #Test Output
                print('Output:')
                print('Latitude:' + str(row[4]))
                print('Longitude:' + str(row[5]))
                print(row)
                #Writing Data
                print('Writing Data')
                csv_writer.writerow(row)
                #Row Done :)
                if row_counter == 400:
                    print('Sequence Complete')
                    return
                row_counter = row_counter + 1
                print('Done row:' + str(row_counter))
                print('*' * 100)


if __name__ == '__main__':
    traverse_csv(sys.argv[1])

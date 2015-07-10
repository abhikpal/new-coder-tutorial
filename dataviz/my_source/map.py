import geojson
import parse


def create_map(data_file):
    """
    Creates a GeoJSON that can be rendered as a map in the GitHub Gist thingy
    """

    # define GeoJSON type
    geo_map = {"type": "FeatureCollection"}

    # create empty list to store points
    item_list = []

    # iterate over the data to create the GeoJSON file
    for index, line in enumerate(data_file):
        # we don't need zero coordinates
        if['X'] == '0' or ['Y'] == '0':
            continue

        # set-up a new dictionary for each iteration
        data = {}

        # assign line items to appropriate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']
                              }
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # append the dictionary to the item_list
        item_list.append(data)

        # add points to the geomap
        for point in item_list:
            geo_map.setdefault('features', []).append(point)

        # write teh dictionary to a GeoJSON file
        with open('file_sf.geojson', 'w') as f:
            f.write(geojson.dumps(geo_map))


def main():
    create_map(parse.parse(parse.DATA_FILE, ','))

if __name__ == '__main__':
    main()

# Unicode CSV
def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

# CSV to JSON for Django
def csv2json(data, model, id_column=False, delim=','):
    data = unicode_csv_reader(data.splitlines(), delimiter=delim)

    # Get fields from header
    fields = data.next()[1:] if id_column else data.next()

    # Create entries dictionary
    pk = 0
    entries = []

    # Create entries
    for row in data:
        if id_column:
            pk = row.pop(0)
        else:
            pk += 1

        entry = {}
        entry['pk'] = int(pk)
        entry['model'] = model
        entry['fields'] = dict(zip(fields, row))

        # Convert to correct data types
        for key, value in entry['fields'].items():
            entry['fields'][key] = int(value) if value.isdigit() else value.strip()
            if value == 'NULL':
                entry['fields'][key] = None

        # Append entry to entries list
        entries.append(entry)

    # Convert to JSON
    return json.dumps(entries, indent=4)
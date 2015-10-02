
import engine_table

HA_ERR_END_OF_FILE = 137

class Example:
    def __init__(self):
        print 'init'

        self.rows = 0

    def rnd_init(self, table):
        comment = engine_table.get_comments(table)

        print comment

        self.hits = [['1', '2'], ['2','3']]
        self.rows = -1

    def rnd_next(self, table):
        print 'rnd_next'
        print table
        print engine_table.fields(table)
        self.rows += 1
        if (self.rows >= len(self.hits)):
            return HA_ERR_END_OF_FILE
        i = 0
        hit = self.hits[self.rows]
        for column in hit:
            engine_table.set_field(table, i, column, len(column))
            i += 1
        return 0

engine = Example


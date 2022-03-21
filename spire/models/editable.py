
class Editable():

    def edit(self):
        # We can already directly edit an object so just use this to mark self as in edit and return self
        self.metadata['in_edit'] = self
        return self

    def save(self):
        if self.metadata['in_edit'] is not None:
            api_client = self.metadata['api_client']
            api_client.save(self)
            self.metadata['in_edit'] = None
        else:
            raise Exception("cannot save an item that doesn't have a pending object to edit")

    def delete(self):
        if hasattr(self, 'metadata'):
            if self.metadata['in_edit'] is not None:
                api_client = self.metadata['api_client']
                api_client.delete(self)
                self.metadata['in_edit'] = None
            else: 
                raise Exception("Cannot delete because we are missing the apiclient object from the current object")
        else:
            raise Exception("Cannot delete an item that doesn't have the necessary metadata to perform the update")

    
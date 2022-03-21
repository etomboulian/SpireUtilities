
class Editable():

    def edit(self):
        self.metadata['in_edit'] = self
        return self.metadata['in_edit']

    def save(self):
        if self.metadata['in_edit'] is not None:
            api_client = self.metadata['api_client']
            api_client.save(self)
            self._remove_metadata()
        else:
            raise Exception("cannot save an item that doesn't have a pending object to edit")

    def delete(self):
        if hasattr(self, 'metadata'):
            if self.metadata['in_edit'] is not None:
                api_client = self.metadata['api_client']
                api_client.delete(self)
                self._remove_metadata()
            else: 
                raise Exception("Cannot delete because we are missing the apiclient object from the current object")
        else:
            raise Exception("Cannot delete an item that doesn't have the necessary metadata to perform the update")

    def _remove_metadata(self):
        if hasattr(self, 'metadata'):
            delattr(self.__class__, 'metadata')
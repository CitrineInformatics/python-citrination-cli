import cli.app
import citrination_client

class App(cli.app.CommandLineApp):

    def main(self):
        """Upload a document"""
        client = citrination_client.CitrinationClient(self.params.api_key, self.params.citrination_host)
        response = client.upload_file(self.params.file, self.params.data_set_id)
        print("Upload a document")
        if response is not None:
            print(response.status_code)
            print(response.json)
        else:
            print("Upload failed due to API server being unable to resolve the upload location.")

    def setup(self):
        """Setup this application."""
        cli.app.CommandLineApp.setup(self)
        self.add_param("-k", "--api_key", help="Citrination API key.", required=True)
        self.add_param("-e", "--citrination_host", help="Citrination host.",
                       default='https://citrination.com', required=False)
        self.add_param("-f", "--file", help="File to upload.", required=True)
        self.add_param("-d", "--data_set_id", help="Dataset id for the upload.", required=True, type=int)

if __name__ == "__main__":
    adder = App()
    adder.run()

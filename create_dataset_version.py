import cli.app
import argparse
import citrination_client

class App(cli.app.CommandLineApp):

    def main(self):
        """Version a Citrination dataset"""
        client = citrination_client.CitrinationClient(self.params.api_key, self.params.citrination_host)
        response = client.create_data_set_version()
        print("Version a Citrination dataset version")
        print(response.status_code)
        if response.status_code == 200:
            print(response.json)
        else:
            print("Data set version creation failed.")

    def setup(self):
        """Setup this application."""
        cli.app.CommandLineApp.setup(self)
        self.add_param("-k", "--api_key", help="Citrination API key.", required=True)
        self.add_param("-e", "--citrination_host", help="Citrination host.",
                       default='https://citrination.com', required=False)
        self.add_param("-d", "--dataset", help="Dataset to operate on.", required=True, type=int)

if __name__ == "__main__":
    adder = App()
    adder.run()

import cli.app
import argparse
import citrination_client

class App(cli.app.CommandLineApp):

    def main(self):
        """Create a Citrination dataset"""
        client = citrination_client.CitrinationClient(self.params.api_key, self.params.citrination_host)
        response = client.create_data_set()
        if response.status_code == 200:
            print("Data set has been created.")
            print(response.content)
        else:
            print("Data set creation failed.")

    def setup(self):
        """Setup this application."""
        cli.app.CommandLineApp.setup(self)
        self.add_param("-k", "--api_key", help="Citrination API key.", required=True)
        self.add_param("-e", "--citrination_host", help="Citrination host.",
                       default='https://citrination.com', required=False)

if __name__ == "__main__":
    adder = App()
    adder.run()

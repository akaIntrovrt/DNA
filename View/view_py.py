from Model.model_py import Model

class View:
    def __init__(self):
        self.model = Model()


    def ShowMenu(self):
        while True:
            print("\n1: Transcribe DNA -> RNA"
                  "\n2: Transcribe RNA -> DNA"
                  "\n3: Show DNA Info"
                  "\n4: Add Type")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\n" * 100)
                print("You chose 2 - Transcribe DNA -> RNA")
                self.model.transcribe()

            if choice == "2":
                print("\n" * 100)
                print("You chose 2 - Transcribe RNA -> DNA")
                self.model.reverce_transcribe()
            if choice == "3":
                print("\n" * 100)
                print("You chose 3 - DNA Info")
                self.model.ShowDNAInfo()
            if(choice == "4"):
                print("You chose 4 - Add Type")
                print("\n" * 100)
                self.model.AddType()

User = View()

User.ShowMenu()
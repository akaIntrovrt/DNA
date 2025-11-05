class Model:
    def __init__(self, DNA="TACGGATCCGATTGA", RNA = "TACGGATCCGATTGA", type=""):
        self._DNA = DNA
        self._RNA = RNA
        self._type = type



    @property
    def DNA(self):
        return self._DNA

    @DNA.setter
    def DNA(self, value):
        self._DNA = value

    @property
    def RNA(self):
        return self._RNA

    @RNA.setter
    def RNA(self, value):
        self._RNA = value

    def transcribe(self):
        self._RNA = self._DNA.replace("T", "U")
        print("-" * 40)
        print('You chose 1 - Transcribe: DNA -> RNA')
        print(f"RNA Before: {self._DNA}"
              f"\nRNA After: {self._RNA}")
        print("-" * 40)

    def reverce_transcribe(self):
        self._DNA = self._RNA.replace("U", "T")
        if self._RNA != "TACGGATCCGATTGA":
            print("-" * 40)
            print('You chose 2 - Transcribe: RNA -> DNA')
            print(f"DNA Before: {self._RNA}"
              f"\nDNA After: {self._DNA}")
            print("-" * 40)
        else:
            print("-" * 40)
            print(f"Сначала переведите ДНК в РНК")
            print("-" * 40)

    def cg_content(self):
        countC = 0
        countG = 0
        for i in range(len(self._DNA)):
            if self._DNA[i] == "C":
                countC += 1
            if self._DNA[i] == "G":
                countG += 1
        sum = countC + countG
        result = sum / len(self._DNA) * 100
        convert = int(result)
        return convert

    def ShowDNAInfo(self):
        countC = 0
        print("-" * 40)
        self._type = "DNA"
        print('You chose 3 - DNA Info')
        print(f"DNA: {self._DNA}  \nLength: {len(self._DNA)}")
        print(f"CG: {self.cg_content()}%")
        print(f"Type: {self._type}")

        print("-" * 40)

    def AddType(self):
        countType = 0
        countC = 0
        countG = 0
        new = input("Enter new type: ") # Это ввод нового ДНК или РНК(Добавлю от себя)
        for i in range(len(new)):
            if new[i] == "U":
                countType += 1
            if countType == 0:
                self._type = "DNA"
            elif countType > 0:
                self._type = "RNA"
        for j in range(len(new)):
            if new[j] == "C":
                countC += 1
            if new[j] == "G":
                countG += 1
        sum = countC + countG
        result = sum / len(new) * 100
        convert = int(result)

        print("-" * 40)
        print(f"Element: {new} \nType: {self._type} \nCG: {convert}%")
        print("-" * 40)





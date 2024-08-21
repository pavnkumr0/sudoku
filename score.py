import csv  




class Score:
    def __init__(self):
        self.scores = []
        self.extract_values()
    
    def extract_values(self):
        try:
            with open('score_track.csv', mode ='r') as file:  
                csvFile = csv.reader(file)  
                for lines in csvFile:
                    if len(lines) >= 2:  # Ensure there are at least two elements in each line
                        self.scores.append(lines)
            
        except FileNotFoundError:
            print("File not found. Please ensure the 'score_track.csv' file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def return_scores(self):
        return self.scores
    
    def print_score(self):
        print(self.scores)



 
# scores = {}
# with open('score_track.csv', mode ='r')as file:  
#             csvFile = csv.reader(file)  
#             for lines in csvFile:
#                 scores[lines[0]] = lines[1]
    

# score_instance = Score()

# scores = score_instance.return_scores()  

# print(scores)
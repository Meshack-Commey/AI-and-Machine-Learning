#External Body Attributes and functions




class ExternalParts:
	#External Body Attributes
	mouth = ['lips','teeth','tonge','saliver','gum']
	face = ['forehead','eyes','nose','cheek','chin',mouth]
	Head = ['hair','ears',face]
	Hands = ['arm','armpit','shoulder','elbow','wrist','palm','fingers','fingernails']
	middle = ['neck','chest','breast','tummy','navel','packs','waist','buttose','penis','back']
	Legs = ['thigh','knee','calf','foot','toe','toenail']
	Body = [Head, middle, Hands, Legs]
	Skin = [Body]

class Bodyfunction:
	def Skin():
		skin = "The skin, the sense organ for feeling. It covers the entire external human body"
		
	def Head():
		head = {
		"hair": "The hair, covers the skull, thereby protects it",
		"ears":"The ears, sense organs for Hearing and Listening",
		"face":" The face is the front view of the head",
		"forehead":"The fore of the face, located on the head",
		"eyes":"The eyes, the sense of sight and observation",
		"nose":"The nose, the sense of breathing and smelling"
		"cheeck":"The Check, the tissue of smile",
		"chin": "The chin is beneath the lips"
		"mouth": "The gateway to input food internally to the body, and/or output speech or vomit",
		"lips": "The Lips opens the mouth and closes it to mute",
		"teeth": "used for grinding that is chewing",
		"tongue": "The sense organ of taste, it indicates how sweet or bitter a sustance is",
		"saliver": "The saliver, a liquid substance that moistens food materials",
		"gum": "The gum serves as a cement that binds the teeth and also supports the tounge in the mouth"
		}
		
	def Middle():
		middle = { }
		
	def Hands():
		hands = { }
		
	def Legs():
		legs = { }
	
	#External Body Functions
class Externalfunctions:
	def feel(Skin):
		print("sense of feeling using skin")
		
	def see(eyes):
		print("Sense of sight using eyes")
		
	def hear(ears):
		print("Sense for hearing using ears")
		
	def breath(nose):
		print("Sense of Breathe using nose")
		
	def taste(tonge):
		print("Sense of Taste using tonge")
		
	def talk(mouth):
		print("Talk using mouth")
		
	def necked(neck):
		print("Rotate or nord the head using neck")
		
	def hold(hands):
		print("Hold using hands")
		
	def walk(legs):
		print("Walk using legs")
		

Read = ExternalParts()
s = Read.Hands
print(s)



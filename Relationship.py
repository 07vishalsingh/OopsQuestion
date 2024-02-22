'''
2.You are designing a relationship management application that helps individuals keep track of their romantic relationships. Design a class hierarchy for different types of relationships such as dating, engaged, and married. Include relevant attributes and methods for each class. Additionally, explain how polymorphism can be applied in this scenario.
'''

# Parent class for Relationship
class Relationship:
    def __init__(self, partner1, partner2, status):
        self.partner1 = partner1
        self.partner2 = partner2
        self.status = status
    
    def get_status(self):
        return self.status

# Subclass for Dating
class Dating(Relationship):
    def __init__(self, partner1, partner2, status="Dating"):
        super().__init__(partner1, partner2, status)
    
    def introduce_partner(self):
        print(f"{self.partner1} and {self.partner2} are dating.")

# Subclass for Engaged
class Engaged(Relationship):
    def __init__(self, partner1, partner2, status="Engaged"):
        super().__init__(partner1, partner2, status)
    
    def announce_engagement(self):
        print(f"{self.partner1} and {self.partner2} are engaged to be married!")

# Subclass for Married
class Married(Relationship):
    def __init__(self, partner1, partner2, status="Married"):
        super().__init__(partner1, partner2, status)
    
    def celebrate_anniversary(self):
        print(f"Happy anniversary to {self.partner1} and {self.partner2}!")

# Example usage
dating_relationship = Dating("Alice", "Bob")
engaged_relationship = Engaged("Carol", "Dave")
married_relationship = Married("Eve", "Frank")

print(dating_relationship.get_status())  # Output: Dating
print(engaged_relationship.get_status())  # Output: Engaged
print(married_relationship.get_status())  # Output: Married

dating_relationship.introduce_partner()  # Output: Alice and Bob are dating.
engaged_relationship.announce_engagement()  # Output: Carol and Dave are engaged to be married!
married_relationship.celebrate_anniversary()  # Output: Happy anniversary to Eve and Frank!

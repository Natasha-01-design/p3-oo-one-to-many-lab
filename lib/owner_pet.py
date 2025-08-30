class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a Pet to this Owner and assign owner to the Pet"""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # class variable to track all instances

    def __init__(self, name, pet_type, owner=None):
        # Validate pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        
        # Validate the owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add to the global list of pets

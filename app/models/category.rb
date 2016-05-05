class Category < ApplicationRecord
    def self.names
      ["Top", "Bottom", "Footwear", "Accessory", "Undergarment", "Other"]
    end
end

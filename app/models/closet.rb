class Closet < ApplicationRecord
  belongs_to :ownner, :class_name => 'User'
  has_many :items

  validates :name, :owner,  presence: true


end

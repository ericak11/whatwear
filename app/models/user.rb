class User < ApplicationRecord
  include Clearance::User
  has_many :closets, foreign_key: 'owner_id'
  has_many :items, through: :closets
  validates :first_name, :last_name, :email, presence: true

  def name
    self.first_name + " " + self.last_name
  end

end

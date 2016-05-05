class User < ApplicationRecord
  include Clearance::User
  has_many :closets

  validates :first_name, :last_name, :email, presence: true
end

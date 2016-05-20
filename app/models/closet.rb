class Closet < ApplicationRecord
   has_attached_file :image,
                    styles: { thumb: "200x200>" },
                    storage: :s3,
                    s3_region: ENV['AWS_REGION'],
                    :s3_credentials => Proc.new{|a| a.instance.s3_credentials }

  belongs_to :owner, :class_name => 'User'
  has_many :items

  validates :name, :owner,  presence: true
  validates_attachment_content_type :image, content_type: /\Aimage\/.*\Z/

  def s3_credentials
    {:bucket => ENV['AWS_BUCKET'] , :access_key_id =>  ENV['P_AWS_ACCESS_KEY_ID'], :secret_access_key =>  ENV['P_AWS_SECRET_ACCESS_KEY'] }
  end

end

class CreateClosets < ActiveRecord::Migration[5.0]
  def change
    create_table :closets do |t|
      t.string :name
      t.string :location
      t.integer :owner_id
      t.attachment :image

      t.timestamps
    end
  end
end

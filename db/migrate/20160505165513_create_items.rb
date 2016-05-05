class CreateItems < ActiveRecord::Migration[5.0]
  def change
    create_table :items do |t|
      t.string :name
      t.string :description
      t.integer :subcategory_id
      t.string :designer
      t.string :size
      t.string :image
      t.integer :quantity, default: 1
      t.string :purchase_date
      t.integer :closet_id

      t.timestamps
    end
  end
end

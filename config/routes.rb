Rails.application.routes.draw do
  root "dashboard#index"

  resources :closets do
    resources :items
  end

  resources :users, controller: :users, only: [:create ]
end

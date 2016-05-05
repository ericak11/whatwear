Rails.application.routes.draw do
  root "dashboard#index"

  resources :items
  resources :closets

  resources :users, controller: :users, only: [:create ]
end

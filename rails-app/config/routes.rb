Rails.application.routes.draw do
  root 'euler#index'
  get 'euler', to: 'euler#index'
  get 'euler/:language', to: 'euler#problems'
end

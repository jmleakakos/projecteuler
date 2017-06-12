Rails.application.routes.draw do
  get 'euler', to: 'euler#index'
  get 'euler/:language', to: 'euler#problems'
end

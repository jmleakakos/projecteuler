class EulerController < ApplicationController
  def index
  end
  
  def problems
    language = params['language']
    extensions = {
      haskell: 'hs',
      ruby: 'rb'
    }

    @language = language.capitalize

    path = "../#{language}/"
    Dir.chdir(path)
      @files = Dir.glob("*.#{extensions[language.to_sym]}").map do |file_name| 
      problem_name = file_name.slice(0..-4)
      problem_text = IO.read(File.expand_path(file_name, path))
      EulerProblem.new(problem_name, problem_text)
    end
  end
end

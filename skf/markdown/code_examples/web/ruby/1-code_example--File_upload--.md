# File upload
-------

## Example:


    // Most of Ruby on Rails developers use specific gem to handle file upload. The most popular gem is to do this is Paperclip.

    // To install Paperclip follow instructions at https://github.com/thoughtbot/paperclip
    // Configuring gem is typical - creating proper model, views and controller.

    // Now something about security - create strong validation rules in model. For example:

    // File: APP_DIR/app/models/photo.rb
    validates_attachment :image,
                        presence: true, # validates if file is proper image
                        content_type: {content_type: %w(image/jpeg image/gif image/png)}, # whitelist content type
                        size: {in: 0..10.kilobytes} # set maximum size of uploading
    validates_attachment_file_name :image, matches: [/^[a-zA-Z0-9]$/] # allow only alphanumerical file names
    // Always upload files outside the website root directory 

    // Paperclip logs every upload action by default. If you want to turn logging on explicite add following line of code
    // to your APP_DIR/config/environments/production.rb
    Paperclip.options[:log] = true

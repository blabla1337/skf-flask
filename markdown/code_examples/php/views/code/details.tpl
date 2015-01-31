<?php

# Copyright 2014 Riccardo ten Cate
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

?>
<!DOCTYPE html>
 
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title><?php echo htmlspecialchars($title); ?> | Article Details</title>
    </head>
    <body>
     
        <?php include HOME . DS . 'includes' . DS . 'menu.inc.php'; ?>
         
        <article>
            <header>
                <h1><?php echo htmlspecialchars($title); ?></h1>
                <p>Published on: <time pubdate="pubdate"><?php echo htmlspecialchars($datePublished); ?></time></p>
            </header>
            <p>
                <?php echo htmlspecialchars($articleBody); ?>
            </p>
        </article>
         
        <a href="/">Back to article list</a>
         
    </body>
</html>
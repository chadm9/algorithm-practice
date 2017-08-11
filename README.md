## Code Example

### Uploading Book Contents to WriteIt
WriteIt assists its writers in the creative writing process by
allowing them to store ideas about their works for review using
the guided writing process.  The following code snippets demonstrate
the uploading of book data to the WriteIt database.
<br><br>
On the front end, writers can fill in information about their work
and click a submit button to upload their input to the database.  
The following code snippet demonstrates the submit button's handle
click function.
```JavaScript
    handleNotes(event){
        //Prevent the default button submit behavior when the
        //user clicks to upload a new notepad.
        event.preventDefault();

        //Get the current user's username from Redux
        var username = this.props.registerResponse.name;
        //Get the title of the book, which is stored in the url.
        var book = this.props.match.params.book;
        //Get the text input that user is attempting to upload.
        var notepad = document.getElementById('text').value;
        //Get the unique database ID of the associated with the 
        //notepad if it existed previouslu.
        var id = this.props.location.search.slice(4);


        //Call the Redux notepad action to send the data to the server
        this.props.notePadAction({
            username: username,
            book: book,
            notepad: notepad,
            id: id
        });
        //Send the user back to the write menu while storing the book
        // they are wooking on in the url.  
        this.props.history.push(`/write/${this.props.match.params.book}`);

    }
```
After the writer clicks submit, the information they entered is sent to 
the WriteIT database for storage.  The following code snippet demonstrates
the back-end storage of the user data on the database.

```JavaScript

//Define the route to store notepad data on WriteIt's database
router.post('/notepad', (req, res)=>{
    //Read in the variables associated with the post request.
	var username = req.body.username;
	var book = req.body.book;
	var notepad = req.body.notepad;
    var id = req.body.id;

    //Define the appropriate SQL queries.  The appropriate queries
    //to use are based on the input data.
    
    //Pull previous notepad entries corresponding to the username and book title.
    var notePadLetterQuery = `SELECT * FROM notepad WHERE username = ? AND book = ? AND notepad = ?`;
    //Define an insert query for new entries.
    var insertNotePadQuery = `INSERT INTO notepad
    	(notepad,username,book) VALUES (?,?,?)`;
    //Define an update query for previous entries
    var updateNotePadQuery = `UPDATE notepad SET notepad='${notepad}' WHERE username='${username}' AND book='${book}';`;

    //If a unique id exists, update the entry corresponding to it.
    if(id!==''){
        var editNotePadQuery = `UPDATE notepad SET notepad='${notepad}' WHERE id='${id}';`;
        connection.query(editNotePadQuery, (error2, results2)=>{
            console.log('update')
            if(error2) throw error2;
            res.json({
                msg: 'Updated'
            })
        })
	}else{
        //If no id exists, and no database entry with the same data exists,
        //write the new entry to the database and send a response to the front-end.
        connection.query(notePadLetterQuery, [username, book, notepad], (error,results)=>{
            if(error) throw error;
            if(results.length === 0){
                connection.query(insertNotePadQuery, [notepad, username, book],(error2, results2)=>{
                    if(error2) throw error2;
                    res.json({
                        msg: 'Inserted'
                    })
                })
            }
        })
	}
});
```


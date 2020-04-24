
(defvar *db* nil)
;; access with > *db*
(defun make-cd (title artist rating ripped)
  ;; usage
  ;; (getf (make-cd "ads" "ads" 7 t) :title)
  (list :title title :artist artist :rating rating :ripped ripped))
(defun add-record (cd) (push cd *db*))
;; usage (add-record (make-cd "Fly" "Dixie Chicks" 8 t))
(defun dump-db ()
  (dolist (cd *db*)
    (format t "~{~a:~10t~a&~}~%" cd)))

(defun prompt-read(prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*)
  )
(defun prompt-for-cd()
  (make-cd
   (prompt-read "Title")
   (prompt-read "Artist")
   (y-or-n-p "Ripped [y/n]")
   (or (parse-integer (prompt-read "Rating") :junk-allowed t) 0)
   )
  )
(defun add-cds ()
  (loop (add-record (prompt-for-cd))
	(if (not (y-or-n-p "Another [y/n]: ")) (return))))

(defun save-db (filename)
  (with-open-file (out filename
                   :direction :output
                   :if-exists :supersede)
    (with-standard-io-syntax
      (print *db* out))))

(defun load-db (filename)
  (with-open-file (in filename)
    (with-standard-io-syntax
      (setf *db* (read in)))))


(defun select-by-artist (artist)
  (remove-if-not
   #'(lambda (cd) (equal (getf cd :artist) artist))
   *db*))

(defun select (selector-fn)
  (remove-if-not selector-fn *db*))

(defun artist-selector (artist)
  #'(lambda (cd) (equal (getf cd :artist) artist)))

(defun where (&key title artist rating (ripped nil ripped-p))
  ;; returns a closure, can be used with select
  ;; > (select (where :artist "asf"))
  ;; or used with funcall
  ;; > (funcall (where :artist "asf") (list :TITLE "asd"))
  #'(lambda (cd)
      (and
       (if title (equal (getf cd :title) title) t)
       (if artist (equal (getf cd :artist) artist) t)
       (if rating (equal (getf cd :rating) rating) t)
       (if ripped-p (equal (getf cd :ripped) ripped) t))))

(defun update (selector-fn &key title artist rating (ripped nil ripped-p))
  (setf *db*
	(mapcar
	 #'(lambda (row)
	     (when (funcall selector-fn row)
	       (if title (setf (getf row :title) title))
	       (if artist   (setf (getf row :artist) artist))
               (if rating   (setf (getf row :rating) rating))
               (if ripped-p (setf (getf row :ripped) ripped))
	       )
	     row
	     ) *db*)))

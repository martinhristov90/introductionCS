### Variable kingdoms refers to the list ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']. 
### Using kingdoms and either slicing or indexing with positive indices, write expressions that produce the following:


- The first item of kingdoms
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[0]
    'Bacteria'
    >>> 
    ```
- The last item of kingdoms
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[-1]
    'Animalia'
    >>> 
    ```
- The list ['Bacteria', 'Protozoa', 'Chromista']
    ```python
     >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
     >>> kingdom[:3]
    ['Bacteria', 'Protozoa', 'Chromista']
    >>> 
    ```
- The list ['Chromista', 'Plantae', 'Fungi']
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[2:5]
    ['Chromista', 'Plantae', 'Fungi']
    >>> 
    ```
- The list ['Fungi', 'Animalia']
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[4:6]
    ['Fungi', 'Animalia']
    >>> 
    ```
- The empty list    
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[:0]
    []
    >>> 
    ```
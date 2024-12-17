export default function CustomButton({onClick,btnClick,customClick}) {

    const clickhandle=()=>{
        onClick();
        customClick();
    }
    
    return (
        <button onClick={clickhandle} className="btn btn-primary">{btnClick}</button>
    )
}